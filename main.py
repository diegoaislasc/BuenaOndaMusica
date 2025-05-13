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

# SONG ---------------------------------------------------------------------------
@app.post("/song/", response_model=schemas.SongCreate, tags=["Songs"])
def create_song(song: schemas.SongCreate, db: Session = Depends(get_db)):
    return services.create_song(db, song)

@app.put("/song/{id}", response_model=schemas.SongResponse, tags=["Songs"])
def update_song(song : schemas.SongCreate, id: int, db: Session = Depends(get_db)):
    db_update = services.update_song(db, id, song)
    if not db_update:
        raise HTTPException(status_code=404, detail="Song not Found")
    return db_update

@app.get("/song/", response_model=list[schemas.SongResponse], tags=["Songs"])
def get_all_songs(db: Session = Depends(get_db)):
    return services.get_all_songs(db)

@app.get("/song/{id}", response_model= schemas.SongResponse, tags=["Songs"])
def get_song_by_id(id: int, db: Session= Depends(get_db)):
    song_queryset = services.get_song_by_id(db, id)
    if song_queryset:
        return song_queryset
    raise HTTPException(status_code= 404, detail="Invalid song id Provided")

@app.get("/song/by-name/{name}", response_model= schemas.SongResponse, tags=["Songs"])
def get_song_by_title(title : str, db: Session = Depends(get_db)):
    song_queryset = services.get_song_by_title(db, title)
    if song_queryset:
        return song_queryset
    raise HTTPException(status_code = 404, detail="Song not Found")


@app.delete("/song/{id}", response_model= schemas.SongResponse, tags=["Songs"])
def delete_song(id: int, db: Session = Depends(get_db)):
    delete_entry = services.delete_song(db,id)
    if delete_entry:
        return delete_entry
    raise HTTPException(status_code=404, detail = "Song not Found")

# SONGWRITER ---------------------------------------------------------------------------
@app.post("/songwriter/", response_model=schemas.SongCreate, tags=["Songwriters"])
def create_songwriter(songwriter: schemas.SongwriterCreate, db: Session = Depends(get_db)):
    return services.create_songwriter(db, songwriter)

@app.put("/songwriter/{id}", response_model=schemas.SongwriterResponse, tags=["Songwriters"])
def update_songwriter(songwriter : schemas.SongwriterCreate, id: int, db: Session = Depends(get_db)):
    db_update = services.update_song(db, id, songwriter)
    if not db_update:
        raise HTTPException(status_code=404, detail="Songwriter not Found")
    return db_update

@app.get("/songwriter/", response_model=list[schemas.SongwriterResponse], tags=["Songwriters"])
def get_all_songwriters(db: Session = Depends(get_db)):
    return services.get_all_songwriters(db)

@app.get("/songwriter/{id}", response_model= schemas.SongwriterResponse, tags=["Songwriters"])
def get_songwriter_by_id(id: int, db: Session= Depends(get_db)):
    songwriter_queryset = services.get_songwriter_by_id(db, id)
    if songwriter_queryset:
        return songwriter_queryset
    raise HTTPException(status_code= 404, detail="Invalid songwriter id Provided")

@app.delete("/song/{id}", response_model= schemas.SongResponse, tags=["Songs"])
def delete_song(id: int, db: Session = Depends(get_db)):
    delete_entry = services.delete_song(db,id)
    if delete_entry:
        return delete_entry
    raise HTTPException(status_code=404, detail = "Song not Found")

# PRODUCER ---------------------------------------------------------------------------
@app.post("/producer/", response_model=schemas.ProducerCreate, tags=["Producers"])
def create_producer(producer: schemas.ProducerCreate, db: Session = Depends(get_db)):
    return services.create_producer(db, producer)

@app.put("/producer/{id}", response_model=schemas.ProducerResponse, tags=["Producers"])
def update_producer(producer : schemas.ProducerCreate, id: int, db: Session = Depends(get_db)):
    db_update = services.update_song(db, id, producer)
    if not db_update:
        raise HTTPException(status_code=404, detail="Producer not Found")
    return db_update

@app.get("/producer/", response_model=list[schemas.ProducerResponse], tags=["Producers"])
def get_all_songs(db: Session = Depends(get_db)):
    return services.get_all_producers(db)

@app.get("/producer/{id}", response_model= schemas.SongResponse, tags=["Producers"])
def get_producer_by_id(id: int, db: Session= Depends(get_db)):
    producer = services.get_producer_by_id(db, id)
    if producer:
        return producer
    raise HTTPException(status_code= 404, detail="Invalid producer id Provided")

@app.get("/song/by-name/{name}", response_model= schemas.SongResponse, tags=["Songs"])
def get_song_by_title(title : str, db: Session = Depends(get_db)):
    song_queryset = services.get_song_by_title(db, title)
    if song_queryset:
        return song_queryset
    raise HTTPException(status_code = 404, detail="Song not Found")


@app.delete("/producer/{id}", response_model= schemas.ProducerResponse, tags=["Producers"])
def delete_producer(id: int, db: Session = Depends(get_db)):
    delete_entry = services.delete_producer(db,id)
    if delete_entry:
        return delete_entry
    raise HTTPException(status_code=404, detail = "Producer not Found")


#SERVICE--------------------------------------------------------------------------------------------------------
@app.get("/service/", response_model=list[schemas.ServiceResponse], tags=["Services"])
def get_all_services(db: Session = Depends(get_db)):
    return services.get_all_services(db)

@app.get("/services/{id}", response_model=schemas.ServiceResponse, tags=["Services"])
def get_service_by_id(id: int, db: Session = Depends(get_db)):
    service_queryset = services.get_service_by_id(db, id)
    if service_queryset:
        return service_queryset
    raise HTTPException(status_code=404, detail="Invalid service id Provided")

@app.get("/services/by-name/{name}", response_model=schemas.ServiceResponse, tags=["Services"])
def get_service_by_name(name: str, db: Session = Depends(get_db)):
    service_queryset = services.get_service_by_name(db, name)
    if service_queryset:
        return service_queryset
    raise HTTPException(status_code=404, detail="Service not Found")

@app.post("/service/", response_model=schemas.ServiceCreate, tags=["Servicios"])
def create_service(service: schemas.ServiceCreate, db: Session = Depends(get_db)):
    return services.create_service(db, service)

@app.put("/service/{id}", response_model=schemas.ServiceResponse, tags=["Servicios"])
def update_service(service: schemas.ServiceCreate, id: int, db: Session = Depends(get_db)):
    db_update = services.update_service(db, service, id)
    if not db_update:
        raise HTTPException(status_code=404, detail="Service not Found")
    return db_update

@app.delete("/services/{id}", response_model=schemas.ServiceResponse, tags=["Servicios"])
def delete_service(id: int, db: Session = Depends(get_db)):
    delete_entry = services.delete_service(db, id)
    if delete_entry:
        return delete_entry
    raise HTTPException(status_code=404, detail="Service not Found")

#STUDIO--------------------------------------------------------------------------------------------------------
@app.get("/studio/", response_model=list[schemas.StudioResponse], tags=["Studios"])
def get_all_studios(db: Session = Depends(get_db)):
    return services.get_all_studios(db)

@app.get("/studios/{id}", response_model=schemas.StudioResponse, tags=["Studios"])
def get_studio_by_id(id: int, db: Session = Depends(get_db)):
    studio_queryset = services.get_studio_by_id(db, id)
    if studio_queryset:
        return studio_queryset
    raise HTTPException(status_code=404, detail="Invalid studio id Provided")

@app.get("/studios/by-name/{name}", response_model=schemas.StudioResponse, tags=["Studios"])
def get_studio_by_name(name: str, db: Session = Depends(get_db)):
    studio_queryset = services.get_studio_by_name(db, name)
    if studio_queryset:
        return studio_queryset
    raise HTTPException(status_code=404, detail="Studio not Found")

@app.post("/studio/", response_model=schemas.StudioCreate, tags=["Studios"])
def create_studio(studio: schemas.StudioCreate, db: Session = Depends(get_db)):
    return services.create_studio(db, studio)

@app.put("/studio/{id}", response_model=schemas.StudioResponse, tags=["Studios"])
def update_studio(studio: schemas.StudioCreate, id: int, db: Session = Depends(get_db)):
    db_update = services.update_studio(db, studio, id)
    if not db_update:
        raise HTTPException(status_code=404, detail="Studio not Found")
    return db_update

@app.delete("/studios/{id}", response_model=schemas.StudioResponse, tags=["Studios"])
def delete_studio(id: int, db: Session = Depends(get_db)):
    delete_entry = services.delete_studio(db, id)
    if delete_entry:
        return delete_entry
    raise HTTPException(status_code=404, detail="Studio not Found")

#EVENT--------------------------------------------------------------------------------------------------------
@app.get("/event/", response_model=list[schemas.EventResponse], tags=["Events"])
def get_all_events(db: Session = Depends(get_db)):
    return services.get_all_events(db)

@app.get("/events/{id}", response_model=schemas.EventResponse, tags=["Events"])
def get_event_by_id(id: int, db: Session = Depends(get_db)):
    event_queryset = services.get_event_by_id(db, id)
    if event_queryset:
        return event_queryset
    raise HTTPException(status_code=404, detail="Invalid event id Provided")

@app.get("/events/by-name/{name}", response_model=schemas.EventResponse, tags=["Events"])
def get_event_by_name(name: str, db: Session = Depends(get_db)):
    event_queryset = services.get_event_by_name(db, name)
    if event_queryset:
        return event_queryset
    raise HTTPException(status_code=404, detail="Event not Found")

@app.post("/event/", response_model=schemas.EventCreate, tags=["Events"])
def create_event(event: schemas.EventCreate, db: Session = Depends(get_db)):
    return services.create_event(db, event)

@app.put("/event/{id}", response_model=schemas.EventResponse, tags=["Events"])
def update_event(event: schemas.EventCreate, id: int, db: Session = Depends(get_db)):
    db_update = services.update_event(db, event, id)
    if not db_update:
        raise HTTPException(status_code=404, detail="Event not Found")
    return db_update

@app.delete("/events/{id}", response_model=schemas.EventResponse, tags=["Events"])
def delete_event(id: int, db: Session = Depends(get_db)):
    delete_entry = services.delete_event(db, id)
    if delete_entry:
        return delete_entry
    raise HTTPException(status_code=404, detail="Event not Found")
