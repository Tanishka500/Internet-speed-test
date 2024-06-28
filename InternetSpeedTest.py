import speedtest
st = speedtest.Speedtest()
option = int(input('''What speed do you want to measure : 
1) Download Speed
2) Upload Speed
3) Ping

Your Choice :'''))

if option == 1:
    print(st.download()/(1025*1025)," mbps")
elif option == 2:
    print(st.upload()/(1025*1025)," mbps")
elif option == 3:
    servername = []
    st.get_servers(servername)
    print(st.results.ping)
else:
    print("Please enter the correct option !")