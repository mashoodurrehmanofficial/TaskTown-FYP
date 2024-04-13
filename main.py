import django,sys,os,json ,traceback
from credentials import *
from utils import * 
from colorama import init, Fore, Back, Style 
# Initialize colorama
init()

def main():
    while True:
        try:
            # 1. Get all queries 
            session = Session(oauth_token=ACCESS_TOKEN)
            queries = list(Config().queries.keys())
            
            # 2. Get all projects for the current query
            for project_query in queries[:]: 
                print(Back.BLUE + Fore.WHITE + f"Searching Projects for Query: {project_query}" + Style.RESET_ALL)
                
                projects = sample_search_projects(query=project_query)
                if projects:
                    projects = projects['projects']
                    for project in projects[:]:
                        print("--------------------------------")
                        url = f"https://www.freelancer.com/projects/{project['seo_url']}"
                        print(f"Project ID: {project['id']}")
                        print(f"\U0001F517 URL = {url}")

                        
                        # 3.1 Check if project proposal has already been submitted
                        # 3.2 Check if project is passing criteria
                        
                        
                        remaining_bids = Config().remaining_bids
                        if remaining_bids<150:
                            print(Back.RED + Fore.WHITE + f"Bids are less than 150 | Remaining Bids = {remaining_bids}" + Style.RESET_ALL)
                        
                        
                        proposal = ""
                        if not ProjectsTable.objects.filter(project_id=int(project['id'])).exists() and isValidProject(project):
                            print("--------------------------------")
                            try:
                                res = sample_place_project_bid(project=project)
                                proposal = res.get("proposal")
                                Config().decrement_remaining_bids()
                            except:
                                print(traceback.format_exc())
                            
                            ProjectsTable(
                                project_id=int(project['id']),
                                title = project['title'],
                                description = project['description'],    
                                proposal = proposal
                            ).save()
                            sleep(seconds=20)
                            
            sleep(minutes=1)           
                            
        except:
            print(traceback.format_exc()) 
            main() 
              
try:
    main()
except:
    print(traceback.format_exc()) 
    main()