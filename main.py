from fastapi import FastAPI, Depends, HTTPException
import services, models, schemas
from db import get_db, engine
from sqlalchemy.orm import Session

app = FastAPI()

#ARTIST--------------------------------------------------------------------------------------------------------
@app.get("/artist/", response_model=list[schemas.ArtistResponse], tags=["Artistas"])
def get_all_artist(db: Session = Depends(get_db)):
    return services.get_all_artists(db)

@app.get("/artists/{id}", response_model= schemas.ArtistResponse, tags=["Artistas"])
def get_artist_by_id(id: int, db: Session= Depends(get_db)):
    artist_queryset = services.get_artist_by_id(db, id)
    if artist_queryset:
        return artist_queryset
    raise HTTPException(status_code= 404, detail="Invalid artist id Provided")

@app.get("/artists/by-name/{name}", response_model= schemas.ArtistResponse, tags=["Artistas"])
def get_artist_by_name(name : str, db: Session = Depends(get_db)):
    artist_queryset = services.get_artist_by_name(db, name)
    if artist_queryset:
        return artist_queryset
    raise HTTPException(status_code = 404, detail="Artist not Found")

@app.post("/artist/", response_model=schemas.ArtistCreate, tags=["Artistas"])
def create_artist(artist : schemas.ArtistCreate, db: Session = Depends(get_db)):
    return services.create_artist(db, artist)

@app.put("/artist/{id}", response_model=schemas.ArtistResponse, tags=["Artistas"])
def update_artist(artist : schemas.ArtistCreate, id: int, db: Session = Depends(get_db)):
    db_update = services.update_artist(db, artist,id)
    if not db_update:
        raise HTTPException(status_code=404, detail="Artist not Found")
    return db_update

@app.delete("/artists/{id}", response_model= schemas.ArtistResponse, tags=["Artistas"])
def delete_artist(id: int, db: Session = Depends(get_db)):
    delete_entry = services.delete_artist(db,id)
    if delete_entry:
        return delete_entry
    raise HTTPException(status_code=404, detail = "Artist not Found")

#ALBUM---------------------------------------------------------------------------------------------------
@app.get("/album/", response_model=list[schemas.AlbumResponse], tags=["Albums"])
def get_all_albums(db: Session = Depends(get_db)):
    return services.get_all_albums(db)

@app.get("/album/{id}", response_model= schemas.AlbumResponse, tags=["Albums"])
def get_album_by_id(id: int, db: Session= Depends(get_db)):
    album_queryset = services.get_album_by_id(db, id)
    if album_queryset:
        return album_queryset
    raise HTTPException(status_code= 404, detail="Invalid album id Provided")

@app.get("/album/by-name/{name}", response_model= schemas.AlbumResponse, tags=["Albums"])
def get_album_by_name(name : str, db: Session = Depends(get_db)):
    album_queryset = services.get_album_by_name(db, name)
    if album_queryset:
        return album_queryset
    raise HTTPException(status_code = 404, detail="Album not Found")

@app.post("/album/", response_model=schemas.AlbumCreate, tags=["Albums"])
def create_album(album : schemas.AlbumCreate, db: Session = Depends(get_db)):
    return services.create_album(db, album)

@app.put("/album/{id}", response_model=schemas.AlbumResponse, tags=["Albums"])
def update_album(album : schemas.AlbumCreate, id: int, db: Session = Depends(get_db)):
    db_update = services.update_album(db, id, album)
    if not db_update:
        raise HTTPException(status_code=404, detail="Album not Found")
    return db_update

@app.delete("/album/{id}", response_model= schemas.AlbumResponse, tags=["Albums"])
def delete_album(id: int, db: Session = Depends(get_db)):
    delete_entry = services.delete_album(db,id)
    if delete_entry:
        return delete_entry
    raise HTTPException(status_code=404, detail = "Album not Found")