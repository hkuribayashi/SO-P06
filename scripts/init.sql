CREATE DATABASE meubanco;

USE meubanco;

create table dados
(
    id    integer      not null auto_increment,
    nome  varchar(255) not null,
    idade integer      not null,
    primary key (id)
);
