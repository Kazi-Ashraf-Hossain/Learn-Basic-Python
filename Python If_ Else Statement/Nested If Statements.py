score = 85
attendance  = 90
submitted = True

if score >=60:
    if attendance >=80:
        if submitted:
            print("Pass with Good Standing")
        else:
            print("Pass but Missing Assignment")
    else:
        print("Pass but low Attendence")
else:
    print("Fail")

