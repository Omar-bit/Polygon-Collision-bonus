def polygon_collision(poly1, poly2):
    test=False
    for x1,y1 in poly1:
        doubt=False
        x2min=min([i for i,g in poly2 ])
        x2max=max([i for i,g in poly2 ])
        for x2,y2 in poly2:
            if x2min<=x1<=x2max:
                y2min=min([g for i,g in poly2 ])
                y2max=max([g for i,g in poly2 ])
                if y2min<=y1<=y2max:
                    test=True
    return test
print(polygon_collision([(0,0), (0,1), (1,1), (1,0)], [(1.2,-3), (2.2,-3), (2.2,0.5), (1.2,0.5)]))