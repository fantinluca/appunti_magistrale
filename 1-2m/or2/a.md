![400](b.png)
Inizio: [2,3,1,4,0], start=0 -> next=start=0, carry=succ[start]=2
Iterazione 1:
	curr=next=0
	next=carry=2
	carry=succ[next]=1
	succ[next]=curr
	array diventa [2,3,0,4,0]
Iterazione 2:
	curr=next=2
	next=carry=1
	carry=succ[next]=3
	succ[next]=curr
	array diventa [2,2,0,4,0]
Iterazione 3:
	curr=next=1
	next=carry=3
	carry=succ[next]=4
	succ[next]=curr
	array diventa [2,2,0,1,0]
Iterazione 4:
	curr=next=3
	next=carry=4
	carry=succ[next]=0
	succ[next]=curr
	array diventa [2,2,0,1,3]
Iterazone 5:
	curr=next=4
	next=carry=0
	mi fermo perchè next=start -> basta carry
	succ[next]=curr
	array diventa [4,2,0,1,3]