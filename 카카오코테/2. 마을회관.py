road = []
cnt = 0
for _ in range(10): 
    road.append(list(input()))

h_x = h_y = m_x = m_y = 0

for i in range(len(road)):
    if 'H' in road[i]:
        h_x = i 
        h_y = road[i].index('H')
    if 'M' in road[i]:
        m_x = i 
        m_y = road[i].index('M')

if h_x < m_x:
    while True:
        if road[h_x+1][h_y] == '.':
            h_x += 1
        else:
            h_y += 1
        

print(x,y)