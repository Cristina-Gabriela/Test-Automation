# class Student:
#     def __init__(self, name, student_number):
#         self.name = name
#         self.student_number = student_number
#         self.clase = []
#
#     def enroll(self, course_running):
#         self.classes.append(course_running)
#         course_running.add_student(self)
#
#
# class Departament:
#     def __init__(self, name, departement_code):
#         self.name = name
#         self.department_code = departement_code
#         self.courses = {}
#
#     def add_course(self, description, course_code, credits):
#         self.courses[course_code] = Course(description, course_code, credits, self)
#         return self.courses[course_code]
#
#
# class Course:
#     def __init__(self, description, course_code, credits, department):
#         self.description = description
#         self.course_code = course_code
#         self.credits = credits
#         self.department = department
#         self.department.add_course(self)
#
#
# class CourseRunning:
#     def __init__(self, course, year):
#         self.course = course
#         self.year = year
#         self.student = []
#
#     def add_student(self, student):
#         self.students.append(student)
#
#
# # dam valori
# maths_dept = Departament('Mathematics and Applied Mathematics', 'MAM')
# mam1000w = maths_dept.add_course('Mathematics 1000', 'MAM1000W', 1)
# mam1000w_2013 = mam1000w.add_running(2013)
#
# # apelam
# bob = Student("Bob", "Smith")
# bob.enrol(mam1000w_2013)


print("")


class Persoana:
    def __init__(self, nume):
        self.nume = nume  # stocare
        self.nume = [nume]
        self.masina = None

    def merge_la_picnic(self):

        if len(self.nume) == 1:
            a = f"{self.nume[0]}, merge la picnic cu"
            print(a)
        else:
            a = f"{self.nume}, merg la picnic cu"  # string interpolation
            print(a)


        if self.masina is not None:
            print(a, self.masina.name)
        else:
            print(a)


    def schimba_nume(self, noul_nume):
        self.nume = self.nume + [noul_nume]

    def schimba_nume_fara_suprascriere(self, noul_nume):
        self.nume.append(noul_nume)

    def cumpara_masina(self, masina):
        self.masina = masina


class Masina:
    def __init__(self, name, putere, pret):
        self.name = name


x = Persoana('Harap Alb ')
x.merge_la_picnic()
x.schimba_nume("Praslea Cel Voinic ")
x.merge_la_picnic()
x.schimba_nume_fara_suprascriere("Costel")
x.merge_la_picnic()

y = Masina("Opel", 100, 2)
x.cumpara_masina(y)
x.merge_la_picnic()

print(x)

#
# class Course_for_melody:
#     def __init__(self, titlu, artist, album, track_number):
#         self.titlu = titlu
#         self.artist = artist
#         self.album = album
#         self.track_number = track_number
#         artist.add_song(self)
#
#
# class Album:
#     def __init__(self, title, artist, year):
#         self.title = title
#         self.artist = artist
#         self.year = year
#
#         self.tracks = []
#         artist.add_album(self)
#
#     def add_track(self, title, artist=None):
#         if artist = None:
#             artist = self.artist
#
#         track_number = len(self.tracks)
#         song = Song(title, artist, self, track_number)
#         self.tracks.append(song)
#
#
# class Artist:
#     def __init__(self, name):
#         self.name = name
#
#         self.albums = []
#         self.songs = []
#
#     def add_album(self, album):
#         self.albums.append(album)
#
#
# class Playlist:
#     def __init__(self, name):
#         self.name = name
#         self.songs = []
#
#     def add_song(self, song):
#         self.songs.append(song)
#
#
# band = Artist("xyz")
# album = Album("xyz1", band, 2000)
# album.add_track("1. Song")
# album.add_track("2. Song (remix)")
# album.add_track("3. Song")
#
# playlist = Playlist("My favourite songs")
#
# for song in album.tracks:
#     playlist.add_song(song)
#
# print("")

# class Courses:
#     def __init__(self, title, name, year):
#         self.title = title
#         self.name = name
#         self.year = year
#         self.track
# class Album:
#     def __init__(self,title,name,year):
#         self.title = title
#         self.name = name
#         self.year = year
#         self.track
# class Playlist:
#     def __init__(self, title, name, year):
#         self.title = title
#         self.name = name
#         self.year = year
