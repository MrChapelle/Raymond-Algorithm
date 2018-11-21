
def restart_node(list_nodes):
	# we reconstruct the graph
	node_destructed = -1
	graph = {}
	for node in list_nodes :
		print("node", node)
		graph[node.number] = [node.holder, node.queue, node.asked, node.using]
	# we find the destructed node
	print(graph)
	print(list_nodes)
	list_nodes_alive = []
	for (key, liste) in graph :
		if key not in list_nodes_alive :
			list_nodes_alive.append(key)
	for (key, liste) in graph :
		for elem in liste[1] :
			if elem not in list_nodes_alive :
				node_destructed = elem
				break
	# we now which node is killed, we have to build : the node
	list_node_children = []
	for (key, liste) in graph :
		if liste[0] == node_destructed :
			list_node_children.append(key)

	# we now that 4 & 5 (for example) 's holder is 3
	list_node_holder = []
	for (key, liste) in graph :
		if node_destructed in liste[1]:
			list_node_holder.append(key)

	#we now that 2 (for example) is the holder of 3
	if len(list_node_holder) != 0 :
		#the destrcuted node is not the root
		node_holder = min(list_node_holder) #we take the min by default
		node_using = False

	node_queue = []
	node_asked = False

	for (key, liste) in graph :
		if key in list_node_children :
			if len(liste[1]) != 0 :
				node_queue.append(liste[1].pop(0))
				node_asked = True
			else :
				pass
		else :
			pass

	# now we can recreate our node

	if node_destructed == 0 :
		Node_0 = Node(node_destructed, node_holder, node_queue, node_using, node_asked)
		Node_0.init_queue()
		print(" [*] Node " + str(node_destructed).encode() + " has been recreated")
	elif node_destructed == 1 :
		Node_1 = Node(node_destructed, node_holder, node_queue, node_using, node_asked)
		Node_1.init_queue()
		print(" [*] Node " + str(node_destructed).encode() + " has been recreated")
	elif node_destructed == 2 :
		Node_2 = Node(node_destructed, node_holder, node_queue, node_using, node_asked)
		Node_2.init_queue()
		print(" [*] Node " + str(node_destructed).encode() + " has been recreated")
	elif node_destructed == 3 :
		Node_3 = Node(node_destructed, node_holder, node_queue, node_using, node_asked)
		Node_3.init_queue()
		print(" [*] Node " + str(node_destructed).encode() + " has been recreated")
	elif node_destructed == 4 :
		Node_4 = Node(node_destructed, node_holder, node_queue, node_using, node_asked)
		Node_4.init_queue()
		print(" [*] Node " + str(node_destructed).encode() + " has been recreated")
	elif node_destructed == 5 :
		Node_5 = Node(node_destructed, node_holder, node_queue, node_using, node_asked)
		Node_5.init_queue()
		print(" [*] Node " + str(node_destructed).encode() + " has been recreated")