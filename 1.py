    net=ipaddress.ip_network(network, False)

    for ip in net:

        ip_addr=str(ip)

        arp_one=Process(target=arp_request,args=(ip_addr,queue))

        arp_one.start()