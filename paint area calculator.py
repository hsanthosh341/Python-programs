def paint_calc(height,width,cover):
    #use round
    can=math.ceil((height*width)/cover)
    print(f'you will need {can} of paint')
test_h=int(input())
test_w=int(input())
coverage=5
paint_calc(height=test_h,width=test_h,cover=coverage)
