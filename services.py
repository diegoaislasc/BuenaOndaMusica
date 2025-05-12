from models import Artist, Album
from sqlalchemy.orm import Session
from typing import Optional
from typing import Optional, Type
from schemas import ArtistCreate, AlbumCreate


# ARTIST-------------------------------------------------------------

# CREATE ARTISTAS
def create_artist(db: Session, artist: ArtistCreate):
    existing = db.query(Artist).filter(
        (Artist.stage_name == artist.stage_name) |
        (Artist.email == artist.email)
    ).first()
    if existing:
        return None  # evitar artistas duplicados
    # new artist
    new_artist = Artist(**artist.dict())
    db.add(new_artist)
    db.commit()
    db.refresh(new_artist)
    return new_artist


# READ ARTISTs
def get_artist_by_id(db: Session, artist_id: int) -> Optional[Artist]:
    return db.query(Artist).filter(Artist.id == artist_id).first()


def get_all_artists(db: Session) -> list[Type[Artist]]:
    return db.query(Artist).all()


def get_artist_by_name(db: Session, artist_name: str) -> Optional[Artist]:
    return db.query(Artist).filter(Artist.stage_name == artist_name).first()


# UPDATE ARTIST
def update_artist(db: Session, artist: ArtistCreate, artist_id: int):
    artist_queryset = db.query(Artist).filter(Artist.id == artist_id).first()
    if artist_queryset:
        for key, value in artist.model_dump().items():
            setattr(artist_queryset, key, value)
            db.commit()
            db.refresh(artist_queryset)
    return artist_queryset


# DELETE ARTIST
def delete_artist(db: Session, id: int):
    artist_queryset = db.query(Artist).filter(Artist.id == id).first()
    if artist_queryset:
        db.delete(artist_queryset)
        db.commit()
    return artist_queryset


# ALBUM----------------------------------------------------------

# CREATE ALBUMS
def create_album(db: Session, album: AlbumCreate):
    existing = db.query(Album).filter(
        (Album.title == album.title)
    ).first()

    if existing:
        return None  # evitar albumes duplicados

    # new album
    new_album = Album(**album.dict())
    db.add(new_album)
    db.commit()
    db.refresh(new_album)
    return new_album


# DELETE ALBUM
def delete_album(db: Session, album_id: int) -> Type[Album] | None:
    album = db.query(Album).filter(Album.id == album_id).first()

    if not album:
        return None

    db.delete(album)
    db.commit()
    return album


# READ ALBUMS
def get_album_by_name(db: Session, album_name: str) -> Optional[Album]:
    return db.query(Album).filter(Album.title == album_name).first()


def get_album_by_id(db: Session, album_id: int) -> Optional[Album]:
    return db.query(Album).filter(Album.id == album_id).first()


def get_all_albums(db: Session) -> list[Type[Album]]:
    return db.query(Album).all()


# UPDATE ALBUMS
def update_album(db: Session, album_id: int, album_data: AlbumCreate) -> Type[Album] | None:
    album_queryset = db.query(Album).filter(Album.id == album_id).first()
    if album_queryset:
        for key, value in album_data.dict(exclude_unset=True).items():
            setattr(album_queryset, key, value)
            db.commit()
            db.refresh(album_queryset)
    return album_queryset

