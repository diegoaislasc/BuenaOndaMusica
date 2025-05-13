from pydantic import BaseModel, EmailStr, constr
from typing import Optional
from datetime import date

# ARTIST SCHEMAS-------------------------------------------------
class ArtistCreate(BaseModel):
    real_name: Optional[str] = None
    stage_name: constr(min_length=2, max_length=255)
    music_genre: Optional[str] = None
    country_of_origin: Optional[str] = None
    email: Optional[EmailStr] = None
    instagram_handle: Optional[constr(min_length=2, max_length=30)] = None

    class Config:
        from_attributes = True


class ArtistResponse(BaseModel):
    id: int
    real_name: Optional[str] = None
    stage_name: str
    music_genre: Optional[str] = None
    country_of_origin: Optional[str] = None
    email: Optional[EmailStr] = None
    instagram_handle: Optional[str] = None

    class Config:
        from_attributes = True

class ArtistUpdate(BaseModel):
    real_name: Optional[str] = None
    stage_name: Optional[constr(min_length=2, max_length=255)] = None
    music_genre: Optional[str] = None
    country_of_origin: Optional[str] = None
    email: Optional[EmailStr] = None
    instagram_handle: Optional[constr(min_length=2, max_length=30)] = None

    class Config:
        from_attributes = True

#ALBUM SCHEMAS-------------------------------------------------------------------
class AlbumCreate(BaseModel):
    title: constr(min_length=1, max_length=255)
    release_date: Optional[date] = None
    artist_id: int

    class Config:
        from_attributes = True

class AlbumResponse(BaseModel):
    id: int
    title: constr(min_length=1, max_length=255)
    release_date: Optional[date] = None
    artist_id: int

    class Config:
        from_attributes = True

class AlbumUpdate(BaseModel):
    title: Optional[constr(min_length=1, max_length=255)] = None
    release_date: Optional[date] = None
    artist_id: Optional[int]

    class Config:
        from_attributes = True


# SONG SCHEMAS --------------------------------------------------------------------------------------
from pydantic import BaseModel, constr
from typing import Optional


class SongCreate(BaseModel):
    title: constr(min_length=1, max_length=255)
    duration: int  # duración en segundos
    album_id: int

    class Config:
        from_attributes = True

class SongUpdate(BaseModel):
    title: Optional[constr(min_length=1, max_length=255)] = None
    duration: Optional[int] = None
    album_id: Optional[int] = None

    class Config:
        from_attributes = True

class SongResponse(BaseModel):
    id: int
    title: str
    duration: int
    album_id: int

    class Config:
        from_attributes = True



