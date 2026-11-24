create table zrz_test_0.employee
(
    id         int auto_increment comment '主键ID'
        primary key,
    name       varchar(50)  null comment '姓名',
    phone      varchar(20)  null comment '手机号',
    email      varchar(100) null comment '邮箱',
    profession varchar(100) null comment '专业',
    age        int          null comment '年龄',
    gender     int          null comment '性别 (1男 2女)',
    status     int          null comment '状态',
    createtime datetime     null comment '创建时间'
)
    comment '用户信息表';

create index ind_pho
    on zrz_test_0.employee (phone);

create index ind_user_pho_age
    on zrz_test_0.employee (phone, age);

create index ind_user_pro_age_sta
    on zrz_test_0.employee (profession, age, status);

