# Ejercicio 7 

DB DIAGRAM -> https://dbdiagram.io/d/64f35b9c02bd1c4a5eda2643

- Crear una app nueva llamada psicomedic.
- En esa app tendremos las tablas de SQL de Psicologos, Pacientes, Citas.
- Los psicologos tendran first_name, last_name, birthdate, email, phone, created_at
- Los pacientes tendran first_name, last_name, birthdate, email, phone, biography, address, created_at.
- Las citas contienen una fecha, titulo, paciente y un psicologo(hacer las relaciones necesarias)
- Crear respectivos psicologos, pacientes y citas con el ORM.
- Hacer las rutas con sus respectivas vistas y templates y mostrar datos de la BD por medio del ORM
1. list_psychologists
2. get_psychologist
3. list_patients
4. get_patient
5. list_appointments
6. get_appointment

URLS
1 - psychologists/
2 - psychologists/id
3 - patients/
4 - patients/id
5 - appointments/
6 - appointments/id