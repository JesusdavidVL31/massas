from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# Configuración de la base de datos
DATABASE_URL = "mysql+mysqlconnector://root:310805310805Jvvv@localhost:3306/masas_bd"

# Configuración de SQLAlchemy
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Probar la conexión a la base de datos
try:
    with engine.connect() as connection:
        print("Conexión exitosa a la base de datos.")
except Exception as e:
    print(f"Error al conectar con la base de datos: {e}")
    raise e

# Inicialización de FastAPI
app = FastAPI()

# Modelo para los usuarios
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), unique=True, index=True)
    password = Column(String(255))  # Guardaremos la contraseña sin cifrar

# Crear las tablas
Base.metadata.create_all(bind=engine)

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Modelos de Pydantic para entrada de datos
class UserCreate(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

# Ruta para registrar usuarios
@app.post("/register/")
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")

    new_user = User(username=user.username, password=user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User registered successfully", "user_id": new_user.id}

# Ruta para iniciar sesión
@app.post("/login/")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if not db_user or db_user.password != user.password:
        raise HTTPException(status_code=401, detail="Incorrect username or password")

    return {"message": "Login successful"}

# Probar que funciona la conexión a la base de datos
@app.get("/")
def root():
    return {"message": "API is running and connected to the database"}
