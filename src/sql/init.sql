create table if not exists users(
    id int primary key,
    password VARCHAR(512) NOT NULL,
    email VARCHAR(512) NOT NULL,
    gender VARCHAR(1) NOT NULL,
    first_name VARCHAR(512) NOT NULL,
    surname VARCHAR(512) NOT NULL,
    phone int NOT NULL,
    role VARCHAR(1) NOT NULL
);

create table if not exists muscles(
    id int primary key,
    title VARCHAR(512) NOT NULL,
    difficulty VARCHAR(512) NOT NULL,
    function VARCHAR(512) NOT NULL
);

create table if not exists gym(
    id int primary key,
    adress VARCHAR(512) NOT NULL,
    phone int NOT NULL,
    work_hours VARCHAR(512) NOT NULL
);

create table if not exists position(
    id int primary key,
    title VARCHAR(512) NOT NULL,
    experience int NOT NULL,
    function VARCHAR(512) NOT NULL
);

create table if not exists trainer(
    id int primary key,
    gender VARCHAR(1) NOT NULL,
    first_name VARCHAR(512) NOT NULL,
    surname VARCHAR(512) NOT NULL,
    number int NOT NULL,
    position_id int NOT NULL,
    foreign key (position_id) references position(id),
    gym_id int NOT NULL,
    foreign key (gym_id) references gym(id)
);

create table if not exists exercise(
    id int primary key,
    title VARCHAR(512) NOT NULL,
    muscles_id int NOT NULL,
    foreign key (muscles_id) references muscles(id),
    difficulty int NOT NULL
);

create table if not exists train(
    id int primary key,
    title VARCHAR(10) NOT NULL,
    dates VARCHAR(10) NOT NULL,
    times VARCHAR(5) NOT NULL,
    trainer_id int NOT NULL,
    foreign key (trainer_id) references trainer(id),
    gym_id int NOT NULL,
    foreign key (gym_id) references gym(id)
);

create table if not exists conn(
    train_id int NOT NULL,
    foreign key (train_id) references train(id),
    exercise_id int NOT NULL,
    foreign key (exercise_id) references exercise(id)
);



insert into users values (1, '123', 'aaa@mail.ru', 'm', 'Pavel', 'Maslukov', 89, 'a');
insert into users values (2, '555', 'mc_krut@mail.ru', 'm', 'Egor', 'Mamamev', 77, 'u');
insert into users values (3, '879', 'lol@gmail.com', 'f', 'Nastya', 'Krohina', 6761, 't');
insert into users values (4, 'paswd', 'boriska@mail.ru', 'f', 'Yulia', 'Borisova', 7575, 'u');
insert into users values (5, 'sosiskakiller', 'aaa@mail.ru', 'm', 'Matvey', 'Kozhivnikov', 909, 'u');


insert into muscles values (1, 'legs', 'high', 'Мышцы ног, отвечающие за движение человека');
insert into muscles values (2, 'press', 'low', 'Мышцы пресса');
insert into muscles values (3, 'chest', 'mid', 'Грудные мышцы');
insert into muscles values (4, 'biceps', 'low', 'Мышцы бицепса');


insert into exercise values (1, 'leg press', 1, 2);
insert into exercise values (2, 'barbell squats', 1, 5);
insert into exercise values (3, 'bench press', 3, 3);
insert into exercise values (4, 'dumbbell lift', 4, 1);


insert into gym values (1, '7th parkovaya', 999, '10:00-22:00');
insert into gym values (2, '11th parkovaya', 998, '11:00-23:00');
insert into gym values (3, 'arbat', 11, '8:00-22:00');
insert into gym values (4, 'baumanskaya', 905, '7:00-24:00');
insert into gym values (5, 'vdnh', 999, '8:00-21:00');


insert into position values (1, 'senior coach', 5, 'Занятия по бодибилдингу');
insert into position values (2, 'coach', 1, 'Проведение тренировок');
insert into position values (3, 'junior coach', 0, 'Помощь по залу');


insert into trainer values (1, 'f', 'Nastya', 'Krohina', 6761, 2, 1);
insert into trainer values (2, 'm', 'Khamzat', 'Iliyasov', 555, 3, 4);
insert into trainer values (3, 'm', 'Stepan', 'Kotov', 3434, 1, 3);
insert into trainer values (4, 'm', 'Pavel', 'Krutoy', 934, 1, 1);
insert into trainer values (5, 'm', 'Victor', 'Uzanin', 5373, 3, 2);


insert into train values (1, 'aerobic', '30.05.24', '12:00', 1, 1);
insert into train values (2, 'fitness', '11.05.24', '17:00', 5, 2);
insert into train values (3, 'arm bomb', '20.05.24', '13:00', 3, 3);
insert into train values (4, 'fitnes', '22.05.24', '12:00', 1, 1);

create table if not exists conn(
    train_id int NOT NULL,
    foreign key (train_id) references train(id),
    exercise_id int NOT NULL,
    foreign key (exercise_id) references exercise(id)
);

insert into conn values (1, 4);
insert into conn values (1, 2);
insert into conn values (2, 1);
insert into conn values (3, 2);
insert into conn values (4, 4);