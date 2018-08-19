import rpc
import time

print("Demo for python-discord-rpc")
client_id = '480690616674811927' #Your application's client ID as a string. (This isn't a real client ID)
rpc_obj = rpc.DiscordIpcClient.for_platform(client_id) #Send the client ID to the rpc module
print("RPC connection successful.")

time.sleep(5)
start_time = time.time()
while True:
    activity = {
            "state": "Active on: Linux Mint",
            "timestamps": {
                "start": start_time
            },
            "assets": {
                "small_text": "ku_small",
                "small_image": "ku_small",
                "large_text": "hype_large",
                "large_image": "hype_large"
            }
        }
    rpc_obj.set_activity(activity)
    time.sleep(30)