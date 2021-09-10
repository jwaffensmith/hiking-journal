/* 
to seed this data, run in terminal:
    psql hikeapp -f db/seed.sql

 */


INSERT INTO main_app_hike(    
    name,
    img_one,
    img_two,
    img_three,
    description,
    location,
    length, 
    elevation_gain,
    hike_rating, 
    hike_date, 
    created_at, 
    user_id)
    VALUES
    ('Mt Si', 
    'https://source.unsplash.com/LOhZNOJc3Ro', 
    '', 
    '', 
    'Hot as hell! And super busy.',
    'Bend, WA', 
    7.2,
    3500,
    3,
    '2021-09-09',
    '2021-09-09 15:42:5',
    '14'
    );

