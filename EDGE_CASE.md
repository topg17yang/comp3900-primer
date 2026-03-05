# Document your edge case here
- To get marks for this section you will need to explain to your tutor:
1) The edge case you identified

When the user is trying to create a new student without providing the required 
field, such as student's name or course. This case is not mentioned spec. If this
was not added, then creating a student without a name or a course will result 
the database be incomplete.

2) How you have accounted for this in your implementation
In the Post/ Student, the system will check to ensure that 
both `name` and `course` are provided. If not, the API returns a `400 Bad Request` 
response with an error message indicating that both fields are required. This ensures the 
integrity of the database






