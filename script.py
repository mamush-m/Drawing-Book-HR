def page_count(n, p):
    pages = []
    forward = 0
    backward = 0
    
    for i in range(0, n + 1, 2):
        page_group = []
        
        page_group.append(i)
        if i < n:
            page_group.append(i+1)
        
        pages.append(page_group)
    
    for i in pages:
        if i[0] == p  or i[1] == p:
            break
        forward += 1
        
    for i in range(1, len(pages) ):
        index = -i
        if len(pages[index]) != 1:
            if pages[index][0] == p or pages[index][-1] == p:
                break
        else:
            if pages[index][0] == p:
                break
        backward += 1
    
    if forward < backward:
        return forward
    elif forward > backward:
        return backward
    else:
        return forward
    

page_count(6, 4)
page_count(7, 3)
page_count(11, 6)
page_count(24, 7)