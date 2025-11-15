def find_max_height(heights):
    max_height =  heights[0]
    
    steps =0
    
    for height in heights:
        steps = +1
        print(f"Step {steps} checking {height} cm")
        if height > max_height:
            max_height = height
            
        print(f"The tallest person is {max_height} cm tall.")
        return max_height, steps
    
