from fastapi import APIRouter, Depends, HTTPException
from starlette import status
from starlette.responses import JSONResponse

from api.deps import get_user_repository
from repository.user_repository import UserRepository
from schema.user import UserSchemaCreate, UserSchemaRead

router = APIRouter()


@router.post("/",response_model=UserSchemaRead, status_code=status.HTTP_201_CREATED)
async def create_new_user(user_in: UserSchemaCreate,
                          repo: UserRepository = Depends(get_user_repository)):
    # Basic exception handling. Detail api exception handling is out of scope for this project.
    print(user_in)

    if not user_in:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid request")

    if repo.exists_by_email(user_in.email):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User already exists")

    db_user = repo.create(user_in)
    if not db_user:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to create user")

    return db_user


@router.get("/{id}")
async def get_user():
    pass


@router.put("/{id}")
async def update_user():
    pass


@router.delete("/{id}")
async def delete_user():
    pass
