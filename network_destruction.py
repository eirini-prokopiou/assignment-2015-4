from collections import defaultdict
import sys
import operator

args = sys.argv

#prwtos tropos:
#args=[0,0,0,0]
#args[1] = '-r'
#args[2] = 2
#args[2] = 4
#args[4] = 'destruction_example_1.txt'

#deuteros tropos:
#args=[0,0,0]
#args[1] = '-c'
#args[2] = 4
#args[3] = 'destruction_example_1.txt'


if(args[1]== '-r'):
    with open(args[4]) as fp:
        nodes = defaultdict(list)
        for line in fp:
            line = line.split()
            if line:
                nodes[int(line[0])].append(int(line[1]))
                nodes[int(line[1])].append(int(line[0]))

    i = 2
    num_nodes = int(args[3])
    r = int(args[2])
    all_keys=[]
    for x in nodes.keys():
        all_keys.append(int(x))
    print("Size: ", len(all_keys), " members: ", all_keys)
    def remove_largest_node(i,num_nodes,r):
        list_values = []

        def get_values(list_values,nodes):
            xxx = list_values
            list_values=[]
            for t in xxx:
                for g in nodes[t]:
                    list_values.append(g)
            return (list_values)

        ci_dic = defaultdict(list)
        for x in nodes.keys():
            length = len(nodes[x])
            list_values=nodes[x]
#            print("edw!!!!!!!!!!", list_values)
            y=0
#            print("to Y einai:", y, "to R einai", r)
            lala=[]
            for y in range (0,r):
                length_before=len(list_values)
#                print("to y einai gia prwth fora", y)
#                print("prin to get", list_values)

                lala = get_values(list_values,nodes)
                list_values=lala

#                print("meta to get",lala, list_values)
                y=+1


            ballir=len(lala)-length_before
            ci=(length-1)*ballir
#            print("CI=", ci)


            ci_dic[x].append(ci)
#            print("ci dictionary:",ci_dic)

        sorted_ci = sorted(ci_dic, key=lambda k: ci_dic[k], reverse=True)
        o=int(0)
        while o < num_nodes:
            print("Removing node: ", sorted_ci[o], " with metric:", ci_dic[sorted_ci[o]])
            o+=1

    remove_largest_node(i,num_nodes,r)


elif(args[1]=='-c'):
    with open(args[3]) as fp:
        nodes = defaultdict(list)
        for line in fp:
            line = line.split()
            if line:
                nodes[int(line[0])].append(int(line[1]))
                nodes[int(line[1])].append(int(line[0]))

    i = 2
    num_nodes = int(args[2])
    split_graph2= defaultdict(list)
    final_dic=defaultdict(list)
    key_list= []
    del_list= []
    all_keys=[]
    for x in nodes.keys():
        all_keys.append(int(x))
    print("Size: ", len(all_keys), " members: ", all_keys)
    counter3=0

    def remove_largest_node(i,num_nodes,key_list,counter3,del_list):
        ordered_nodes = sorted(nodes, key=lambda k: len(nodes[k]), reverse=True)
        # poia keys periexoun to value 25  nodes[ordered_nodes[0]] i ta values tou 25:
        values_of_first = nodes[ordered_nodes[0]]

        length = len(values_of_first)
        x=0
        deleted_values= list()
        while x < length:
            deleted_values.append(values_of_first[0])
            nodes[values_of_first[0]].remove(ordered_nodes[0])
            nodes[ordered_nodes[0]].remove(values_of_first[0])

            if ordered_nodes[0] not in del_list:
                del_list.append(ordered_nodes[0])
#            print ("oi values of first einai :", values_of_first, " to x einai: ", x, "to lenght einai: ", length)
            x += 1

        print("Removing node: ", ordered_nodes[0], " with metric: ", len(deleted_values))

#        print("largest node:", ordered_nodes[0], "values of largest node are: ", deleted_values)
#        print("eirini!!! ", nodes)

        largest_node = ordered_nodes[0]

        if len(key_list)==0:
            for x in nodes.keys():
                key_list.append(int(x))
        key_list.remove(largest_node)

        values_of_first = nodes[largest_node]
        counter1=0
        counter2=0
        for x in deleted_values:
#            print("ti times exei  to key???",x,"times: ", nodes[x])
            if len(nodes[x])== 0:
                    counter3 +=1
#                    print ("den sundeetai me kanena!!!. O counter3 einai: ",counter3 )
                    split_graph2[int(counter3)].append(int(x))
                    key_list.remove(x)
            for y in nodes[x]:
                counter2 +=1
#                print("to split graph 2 einai:", split_graph2)
                if y in deleted_values and not split_graph2:
                        counter1 +=1
#                        print("to",  y, "einai mesa sta deleted")
#                print("counter1 is:", counter1, "counter2 is" ,counter2)
                if counter1 == counter2:

#                    print ("to make a new and to delete from the previous")
                    split_graph2[int(counter3)].append(int(x))
                    split_graph2[int(counter3)].append(int(y))
                    key_list.remove(x)
                    key_list.remove(y)
#                print ("to length tou nodes einai", len(nodes[x]))
            counter1=0
            counter2=0


        print("Size: ", len(key_list), " members: ", key_list)

        for k,v in split_graph2.items():
            print("Size: ", len(v), " members: ", v)

        for b in del_list:
            print("Size: ", 1, " members: ", [b])


        if i<=num_nodes:
            i+=1
            remove_largest_node(i,num_nodes,key_list, counter3, del_list)


    remove_largest_node(i,num_nodes,key_list, counter3, del_list)
