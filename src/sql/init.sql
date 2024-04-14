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
    mgroup VARCHAR(512) NOT NULL,
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







