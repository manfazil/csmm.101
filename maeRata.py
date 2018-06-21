def maeRata(state):
    posIdeal=[(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
    n=3
    distancia=0
    for i,item in enumerate(state):
        if item !=0:
            curX=i/n
            curY=i%n
            offset= abs(curX-posIdeal[item-1][0])+abs(curY-posIdeal[item-1][1])
            distancia+=offset            
    return distancia
                        
