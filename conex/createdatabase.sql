CREATE TABLE rol (
  id int NOT NULL AUTO_INCREMENT primary key,
  nombre varchar(50)
);

CREATE TABLE departamento (
  id int NOT NULL AUTO_INCREMENT primary key,
  nombre varchar(50) NOT NULL ,
  id_gerente int 
);


CREATE TABLE usuario (
  id_usuario int NOT NULL,
  id_rol int not null,
  password varchar(200) not null
);


CREATE TABLE empleado (
  id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
  nombre varchar(50) NOT NULL,
  apellido varchar(50) NOT NULL,
  correo varchar(100) NOT NULL,
  telefono varchar(20) NOT NULL,
  salario int NOT NULL,
  fecha_inicio date NOT NULL,
  direccion varchar(150) NOT NULL,
  id_departamento int NULL
);


alter table empleado add constraint empleado_departamento foreign key (id_departamento) references departamento(id);
alter table usuario add constraint id_empleado_usuario foreign key (id_usuario) references empleado(id);
alter table ususario add constraint rol_usuario foreign key (id_rol) references rol(id);
alter table departamento add constraint gerente_departamento foreign key (id_gerente) references empleado(id);

DELIMITER //
CREATE  PROCEDURE InsertarEmpleado_Usuario(
    IN p_nombre VARCHAR(50),
    IN p_apellido VARCHAR(50),
    IN p_correo VARCHAR(100),
    IN p_telefono VARCHAR(20),
    IN p_salario INT,
    IN p_fecha_inicio DATE,
    IN p_direccion VARCHAR(150),
    IN p_id_rol INT,
    IN p_password varchar(200)
)
BEGIN
    DECLARE v_id_empleado INT;

    -- Insertar datos en la tabla empleado
    INSERT INTO empleado (nombre, apellido, correo, telefono, salario, fecha_inicio, direccion) 
    VALUES (p_nombre, p_apellido, p_correo, p_telefono, p_salario, p_fecha_inicio, p_direccion);

    -- Obtener el ID recién insertado
    SET v_id_empleado = LAST_INSERT_ID();

    -- Insertar datos en la tabla usuario utilizando el ID del empleado
    INSERT INTO usuario (id_usuario, password, id_rol) 
    VALUES (v_id_empleado, p_password, p_id_rol);
END//
DELIMITER ;


DELIMITER //

CREATE PROCEDURE eliminarEmpleado(IN nombreEmpleado VARCHAR(50))
BEGIN
  DELETE FROM usuario
  WHERE id_usuario = (
    SELECT id 
    FROM empleado 
    WHERE LOWER(nombre) LIKE LOWER(nombreEmpleado)
  );

  DELETE FROM empleado
  WHERE LOWER(nombre) LIKE LOWER(nombreEmpleado);
END; // DELIMITER;

