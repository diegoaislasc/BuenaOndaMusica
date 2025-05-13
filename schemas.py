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


# PRODUCER SCHEMAS --------------------------------------------------------------------------------------
class ProducerCreate(BaseModel):
    name: str
    specialty: Optional[str] = None

    class Config:
        from_attributes = True


class ProducerUpdate(BaseModel):
    name: Optional[str] = None
    specialty: Optional[str] = None

    class Config:
        from_attributes = True

class ProducerResponse(BaseModel):
    id: int
    name: str
    specialty: Optional[str] = None

    class Config:
        from_attributes = True


# SERVICE SCHEMAS --------------------------------------------------------------------------------------
class ServiceCreate(BaseModel):
    name: constr(min_length=2,max_length=255)
    description: Optional[str] = None
    price: float

    class Config:
        from_attributes=True


class ServiceResponse(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float

    class Config:
        from_attributes=True


class ServiceUpdate(BaseModel):
    name: Optional[constr(min_length=2,max_length=255)] = None
    description: Optional[str] = None
    price: Optional[float] = None

    class Config:
        from_attributes = True


# STUDIO SCHEMAS ----------------------------------------------------------------------------------
class StudioCreate(BaseModel):
    name: constr(min_length=1, max_length=255)
    address :Optional[str] = None

    class Config:
        from_attributes = True


class StudioResponse(BaseModel):
    id: int
    name: str
    address: Optional[str] = None

    class Config:
        from_attributes = True


class StudioUpdate(BaseModel):
    name: Optional[constr(min_length=1, max_length=255)] = None
    address: Optional[constr(min_length=1, max_length=255)] = None

    class Config:
        from_attributes = True


# EVENT SCHEMA -----------------------------------------------------------------------------
from datetime import date

# Properties to receive on item creation
class EventCreate(BaseModel):
    name: Optional[str] = None
    event_date: Optional[date] = None
    location: Optional[str] = None
    address: Optional[str] = None

    class Config:
        from_attributes = True

# Properties to receive on item update
class EventUpdate(BaseModel):
    name: Optional[constr(min_length=1)] = None
    event_date: Optional[date] = None
    location: Optional[constr(min_length=3, max_length=255)] = None
    address: Optional[str] = None

    class Config:
        from_attributes = True

# Properties to return to client
class EventResponse(BaseModel):
    id: int
    name: Optional[str] = None
    event_date: date = None
    location: Optional[str] = None
    address: Optional[str] = None

    class Config:
        from_attributes = True

# SONGWRITER SCHEMAS------------------------------------------------------------------------------
class SongwriterCreate(BaseModel):
    name: str
    country_of_origin: Optional[str] = None
    music_genre: Optional[str] = None

    class Config:
        from_attributes = True

class SongwriterResponse(BaseModel):
    id: int
    name: str
    country_of_origin: Optional[str] = None
    music_genre: Optional[str] = None

    class Config:
        from_attributes = True

class SongwriterUpdate(BaseModel):
    name: Optional[str] = None
    country_of_origin: Optional[str] = None
    music_genre: Optional[str] = None

    class Config:
        from_attributes = True
