import pandas

student_dict = {
    "student": ["Tai", "Leon", "Jo"],
    "score": [56, 98, 76]
}

# Looping through dictionaries
# for (key,value) in student_dict.item():
# print(value)
# or.. {new_key:new_value for (index, row) in df.iterrows()}


student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# Loop through df
# for (key,value) for student_data_frame.items()
# print(value)

# Loop through rows in df
for(index, row) in student_data_frame.iterrows():
    print(index)
    if row.student == "Tai":
        print(row.score)


