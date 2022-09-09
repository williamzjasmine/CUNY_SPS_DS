filename_str = 'DATA_607-Assignment_2-Movie_Ratings_Survey.csv'

ratings_list = []
people_list = []
movies_list = []

with open(filename_str, 'r') as file_to_read:
    lines = file_to_read.readlines()
    for line in lines[1:]: # skip header w/ question titles
        line_arr = line.split(',')
        name = line_arr[0].replace('"', '')
        gender = line_arr[1].replace('"', '')
        age = line_arr[2].replace('"', '')
        job = line_arr[3].replace('"', '')
        shining_rating = line_arr[4].replace('"', '')
        it_rating = line_arr[5].replace('"', '')
        raiders_rating = line_arr[6].replace('"', '')
        avatar_rating = line_arr[7].replace('"', '')
        caddy_rating = line_arr[8].replace('"', '')
        hangover_rating = line_arr[9].replace('"', '')
        ssr_rating = line_arr[10].replace('"', '')
        sn_rating = line_arr[11].replace('"', '')
        f911_rating = line_arr[12].replace('"', '')
        jdos_rating = line_arr[13].replace('"', '')
        people_list.append([name, gender, age, job])
        ratings_list.append([name, 'The Shining', shining_rating])
        ratings_list.append([name, 'It (2017)', it_rating])
        ratings_list.append([name, 'Indiana Jones: Raiders of the Lost Ark', raiders_rating])
        ratings_list.append([name, 'Avatar', avatar_rating])
        ratings_list.append([name, 'Caddyshack', caddy_rating])
        ratings_list.append([name, 'The Hangover', hangover_rating])
        ratings_list.append([name, 'The Shawshank Redemption', ssr_rating])
        ratings_list.append([name, 'The Social Network', sn_rating])
        ratings_list.append([name, 'Fahrenheit 9/11', f911_rating])
        ratings_list.append([name, 'Jiro Dreams of Sushi', jdos_rating.replace('\n', '')])

movies_list.append(['The Shining', 'Horror', '1980'])
movies_list.append(['It (2017)', 'Horror', '2017'])
movies_list.append(['Indiana Jones: Raiders of the Lost Ark', 'Action/Adventure', '1981'])
movies_list.append(['Avatar', 'Action/Adventure', '2009'])
movies_list.append(['Caddyshack', 'Comedy', '1980'])
movies_list.append(['The Hangover', 'Comedy', '2009'])
movies_list.append(['The Shawshank Redemption', 'Drama', '1994'])
movies_list.append(['The Social Network', 'Drama', '2010'])
movies_list.append(['Fahrenheit 9/11', 'Documentary', '2004'])
movies_list.append(['Jiro Dreams of Sushi', 'Documentary', '2011'])

movies_data = []
people_data = []
rating_data = []
for row in movies_list:
    movies_data.append(",".join(row)+ '\n')

for row in ratings_list:
    rating_data.append(",".join(row) + '\n')

for row in people_list:
    people_data.append(",".join(row)+ '\n')

with open('respondents.csv', 'w') as file_to_write:
    file_to_write.writelines(people_data)

with open('movies.csv', 'w') as file_to_write:
    file_to_write.writelines(movies_data)

with open('ratings.csv', 'w') as file_to_write:
    file_to_write.writelines(rating_data)
