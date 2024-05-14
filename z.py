import asyncio
from channels.layers import get_channel_layer

# Get the channel layer
channel_layer = get_channel_layer()

async def send_test_message():
    # Use async_to_sync to send a message
    await channel_layer.send('test_channel', {'type': 'hello'})

# Run the asynchronous function
asyncio.run(send_test_message())
