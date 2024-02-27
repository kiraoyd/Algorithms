
#------THE PARTY INVITE PROBLEM----BFS adjacency list use example ----------#
#We are throwing a surprise party for our friend Alma.
#We can invite exactly 10 people, including Alma, prioritizing Alma's closest friends and then branching out to invite friends of Alma's friends.
#Who do we invite based on Alma's social network graph?
def bfs_party(social_network, host, party_size, network_size):
    #host is the source node here for this problem
    #social_network is a dictionary, the key is the nodes number, the value is a list of that nodes neighbors

    invited = [] #tracks who we have invited so far
    #Note: This implementation only requires the invited list to work, there is no need for a "visited" list

    #Edge Case:
    #If we try to invite more people than in the network, just invite EVERYONE
    if network_size <= party_size:
        #add the entire network to invited and return
        invited = list(social_network.keys()) #grab all keys, store to list
        return invited

    #------------BFS Traversal code - over an Adjacency List -----------


    #Only nodes that have been visited already, get added to the queue
    queue = [] #holds onto which nodes we still need to visit the neighbors of
    queue.append(host) #The host is visited, as this is the node we start from, so we add it to the queue
    invited.append(host) #consider our host invited, it's their party after all

    #We will need to track how many people have been invited so far, so we can stop when we hit the party_size
    count = 1 #host has been invited, so start count at 1 to include them

    #We will always invite the people closest to host first
    #Keep traversing as long as we have nodes in the queue AND we still have party-spots to fill
    while queue and count < party_size:
        current_node = queue.pop(0) #grab the first node in the queue...
        #...visit the current_nodes neighbors

        #-----The following code block is specific to traversing an adjacency list (dictionary)------
        friends_of_current = social_network[current_node] #get list of this friends, friends
        size = len(friends_of_current)
        #Traverse the friends_of_current list to invite each of this friends, closest friends
        index = 0
        #keep visiting friends and inviting them, until we've visited all the current nodes friends or we've hit the party_size
        while index < size and count < party_size:
            #Add the person to the invited list if not already there, we'd only be inside this loop if we still have party spots left to fill
            if friends_of_current[index] not in invited:
                queue.append(friends_of_current[index]) #add friend of current friend to queue
                invited.append(friends_of_current[index]) #mark them as invited
                count += 1
            index += 1 #check the next closest friend of this current node


    return invited #Once the BFS traversal terminates, this will hold all the nodes / people we invited

#The party problem could translate from Social Networks to maps:
# --> find the 10 restaurants closest to your Focation
# --> Find the 5 uber cars closest to your location
# ...etc



#----------MAIN CALLING ROUTINE----------


#Adjacency List using an example graph where the nodes are numbers from 1 to total_nodes
network = {
    1:[2,7],
    2:[3,5,6,8],
    3:[2,6],
    4:[5,8,9],
    5:[2,4],
    6:[2,3],
    7:[1],
    8:[4,2],
    9:[4,10],
    10:[9],
}


host = 2
party_size = 8
network_size = 10
invited = bfs_party(network, host, party_size, network_size)
print(f"\nIf people really were just numbers (LIES!), then these people are coming to the party: {invited}")


#Adjacency List using a different graph, and representing the nodes as actual text / strings
futurama = {
    "bender":["fry","hedonism bot", "calculon", "roberto", "beer"],
    "hedonism bot":["bender"],
    "calculon":["bender"],
    "roberto":["bender"],
    "beer":["bender"],
    "fry":["bender", "leela"],
    "leela":["fry", "nibbler", "amy", "kif", "hermes"],
    "nibbler":["leela"],
    "amy":["leela", "kif"],
    "kif":["leela", "amy"],
    "hermes":["leela"],
}

host = "fry"
party_size = 8
network_size = 11
invited = bfs_party(futurama, "fry", party_size, network_size)
print(f"\nThese characters from Futurama are coming to {host}'s party: {invited}")