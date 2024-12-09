import speedtest

st = speedtest.Speedtest()

option = int(input('''What speed do you want to measure:
1) Download speed
2) Upload speed
3) Ping
Your Choice: '''))

if option == 1:
    print(st.download()/(1025*1025), "Mbps")

elif option == 2:
    print(st.upload()/(1025*1025), "Mbps")

elif option == 3:
    servername = []
    st.get_servers(servername)
    print(st.results.ping)

else:
    print("Choose the correct option")