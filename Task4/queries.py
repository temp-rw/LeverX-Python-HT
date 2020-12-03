num_of_students_in_rooms = "\
SELECT rooms.id, rooms.name, COUNT(s.id) AS StudentsInRoom \
FROM rooms \
LEFT JOIN students s ON rooms.id = s.room \
    GROUP BY rooms.id \
    ORDER BY rooms.id;\
"

top5_rooms_lowest_avg_age = """\
SELECT rooms.id, rooms.name \
FROM rooms \
LEFT JOIN students s on rooms.id = s.room \
    GROUP BY rooms.id \
    ORDER BY AVG(DATEDIFF(NOW(), s.birthday)) \
LIMIT 5; \
"""

top5_rooms_biggest_age_diff = """ \
SELECT rooms.id, rooms.name \
FROM rooms \
LEFT JOIN students s on rooms.id = s.room \
    GROUP BY rooms.id \
    ORDER BY MAX(DATEDIFF(NOW(), s.birthday)) DESC \
LIMIT 5; \
"""

rooms_with_diff_sex = """
SELECT rooms.id, rooms.name \
FROM rooms \
LEFT JOIN students s ON rooms.id = s.room \
    GROUP BY rooms.id \
    HAVING COUNT(distinct s.sex) > 1; \
"""

query_tuple = (num_of_students_in_rooms, top5_rooms_lowest_avg_age, top5_rooms_biggest_age_diff, rooms_with_diff_sex)
