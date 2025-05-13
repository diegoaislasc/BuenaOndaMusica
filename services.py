from models import Artist, Album, Song, Producer, Songwriter, Service, Studio, Event
from sqlalchemy.orm import Session
from typing import Optional
from typing import Optional, Type
from schemas import ArtistCreate, AlbumCreate, SongCreate, ProducerCreate, SongwriterCreate, ServiceCreate, StudioCreate, EventCreate


# ARTIST-------------------------------------------------------------
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

def get_artist_by_id(db: Session, artist_id: int) -> Optional[Artist]:
    return db.query(Artist).filter(Artist.id == artist_id).first()

def get_all_artists(db: Session) -> list[Type[Artist]]:
    return db.query(Artist).all()

def get_artist_by_name(db: Session, artist_name: str) -> Optional[Artist]:
    return db.query(Artist).filter(Artist.stage_name == artist_name).first()

def update_artist(db: Session, artist: ArtistCreate, artist_id: int):
    artist_queryset = db.query(Artist).filter(Artist.id == artist_id).first()
    if artist_queryset:
        for key, value in artist.model_dump().items():
            setattr(artist_queryset, key, value)
            db.commit()
            db.refresh(artist_queryset)
    return artist_queryset

def delete_artist(db: Session, id: int):
    artist_queryset = db.query(Artist).filter(Artist.id == id).first()
    if artist_queryset:
        db.delete(artist_queryset)
        db.commit()
    return artist_queryset


# ALBUM----------------------------------------------------------
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

def delete_album(db: Session, album_id: int) -> Type[Album] | None:
    album = db.query(Album).filter(Album.id == album_id).first()

    if not album:
        return None

    db.delete(album)
    db.commit()
    return album

def get_album_by_name(db: Session, album_name: str) -> Optional[Album]:
    return db.query(Album).filter(Album.title == album_name).first()

def get_album_by_id(db: Session, album_id: int) -> Optional[Album]:
    return db.query(Album).filter(Album.id == album_id).first()

def get_all_albums(db: Session) -> list[Type[Album]]:
    return db.query(Album).all()

def update_album(db: Session, album_id: int, album_data: AlbumCreate) -> Type[Album] | None:
    album_queryset = db.query(Album).filter(Album.id == album_id).first()
    if album_queryset:
        for key, value in album_data.dict(exclude_unset=True).items():
            setattr(album_queryset, key, value)
            db.commit()
            db.refresh(album_queryset)
    return album_queryset

# SONG ----------------------------------------------------------
def create_song(db: Session, song: SongCreate):
    existing = db.query(Song).filter(
        (Song.title == song.title) |
        (Song.id == song.id.id)
    ).first()

    if existing:
        return None

    new_song = Song(**song.dict())
    db.add(new_song)
    db.commit()
    db.refresh(new_song)
    return new_song

def get_all_songs(db: Session) -> list[Type[Song]]:
    return db.query(Song).all()

def get_song_by_id(db: Session, song_id: int) -> Optional[Song]:
    return db.query(Song).filter(Song.id == song_id).first()

def get_song_by_title(db: Session, title: str) -> Optional[Song]:
    return db.query(Song).filter(Song.title.ilike(f"%{title}%")).first()

def update_song(db: Session, song_id: int, song_data: SongCreate) -> Type[Song] | None:
    song_queryset = db.query(Song).filter(Song.id == song_id).first()
    if not song_queryset:
        return None

    for key, value in song_data.dict(exclude_unset=True).items():
        setattr(song_queryset, key, value)

    db.commit()
    db.refresh(song_queryset)
    return song_queryset

def delete_song(db: Session, song_id: int) -> Type[Song] | None:
    song = db.query(Song).filter(Song.id == song_id).first()
    if not song:
        return None

    db.delete(song)
    db.commit()
    return song

# PRODUCER ----------------------------------------------------------
def create_producer(db: Session, producer: ProducerCreate) -> Producer:
    existing = db.query(Producer).filter(
        Producer.id == producer.id
    ).first()

    if existing:
        return None

    new_producer = Producer(**producer.dict())
    db.add(new_producer)
    db.commit()
    db.refresh(new_producer)
    return new_producer

def get_producer_by_id(db: Session, producer_id: int) -> Producer | None:
    return db.query(Producer).filter(Producer.id == producer_id).first()

def get_all_producers(db: Session) -> list[Type[Producer]]:
    return db.query(Producer).all()

def get_producer_by_name(db: Session, name: str) -> Producer | None:
    return db.query(Producer).filter(Producer.name == name).first()

def update_producer(db: Session, producer_id: int, updates: ProducerCreate) -> Type[Producer] | None:
    producer = db.query(Producer).filter(Producer.id == producer_id).first()
    if not producer:
        return None
    for key, value in updates.dict(exclude_unset=True).items():
        setattr(producer, key, value)
    db.commit()
    db.refresh(producer)
    return producer

def delete_producer(db: Session, producer_id: int) -> Type[Producer] | None:
    producer = db.query(Producer).filter(Producer.id == producer_id).first()
    if not producer:
        return None
    db.delete(producer)
    db.commit()
    return producer


# SONGWRITER ----------------------------------------------------------
def create_songwriter(db: Session, songwriter: SongwriterCreate) -> Songwriter:
    existing = db.query(Songwriter).filter(
        Songwriter.id == songwriter.id
    ).first()

    if existing:
        return None

    new_songwriter = Songwriter(**songwriter.dict())
    db.add(new_songwriter)
    db.commit()
    db.refresh(new_songwriter)
    return new_songwriter

def get_songwriter_by_id(db: Session, songwriter_id: int) -> Optional[Songwriter]:
    return db.query(Songwriter).filter(Songwriter.id == songwriter_id).first()
def get_all_songwriters(db: Session) -> list[Type[Songwriter]]:
    return db.query(Songwriter).all()

def update_songwriter(db: Session, songwriter_id: int, songwriter_data: SongwriterCreate) -> Type[Songwriter] | None:
    songwriter = db.query(Songwriter).filter(Songwriter.id == songwriter_id).first()
    if not songwriter:
        return None

    for key,value in songwriter_data.dict(exclude_unset=True).items():
        setattr(songwriter, key,value)

        db.commit()
        db.refresh(songwriter)
        return songwriter

def delete_songwriter(db: Session, song_id: int) -> Type[Songwriter] | None:
    songwriter = db.query(Songwriter).filter(Songwriter.id == song_id).first()
    if not songwriter:
        return None

    db.delete(songwriter)
    db.commit()
    return songwriter

# SERVICE ----------------------------------------------------------
def create_service(db: Session, service: ServiceCreate) -> Service | None:
    existing = db.query(Service).filter(
        Service.id == service.id
    ).first()

    if existing:
        return None

    new_service = Service(**service.dict())
    db.add(new_service)
    db.commit()
    db.refresh(new_service)
    return new_service

def get_service_by_id(db: Session, service_id: int) -> Service | None:
    return db.query(Service).filter(Service.id == service_id).first()

def get_all_services(db: Session) -> list[Type[Service]]:
    return db.query(Service).all()

def get_service_by_name(db: Session, name: str) -> Service | None:
    return db.query(Service).filter(Service.name == name).first()

def update_service(db: Session, service_id: int, service_data: ServiceCreate) -> Type[Service] | None:
    service = db.query(Service).filter(Service.id == service_id).first()
    if not service:
        return None
    for key, value in service_data.dict(exclude_unset=True).items():
        setattr(service, key, value)
    db.commit()
    db.refresh(service)
    return service

def delete_service(db: Session, service_id: int) -> Type[Service] | None:
    service = db.query(Service).filter(Service.id == service_id).first()
    if not service:
        return None
    db.delete(service)
    db.commit()
    return service

# STUDIO ----------------------------------------------------------
def create_studio(db: Session, studio: StudioCreate) -> Studio | None:
    #Revisa si hay un estudio con el mismo nombre
    existing = db.query(Studio).filter(Studio.name == studio.name).first()
    if existing:
        return None
    #Convierte el objeto StudioCreate a un objeto Studio
    new_studio = Studio(**studio.dict())
    #Guarda el nuevo estudio en la bd
    db.add(new_studio)
    db.commit()
    db.refresh(new_studio)

    #Devuelve el estudio creado
    return new_studio

def get_all_studios(db: Session) -> list[Type[Studio]]:
    return db.query(Studio).all()  #hace la consulta select * from studio

def get_studio_by_id(db: Session, studio_id : int) -> Optional[Studio]:
    return db.query(Studio).filter(Studio.id == studio_id).first()

def get_studio_by_name(db: Session, name: str) -> Optional[Studio]:
    return db.query(Studio).filter(Studio.name == name).first()

def update_studio(db: Session, studio_id: int, studio_data: StudioCreate) -> Type[Studio] | None:
    #Busca el estudio con ese id y si no lo encuentra devuelve none
    studio = db.query(Studio).filter(Studio.id == studio_id).first()
    if not studio:
        return None

    #actualiza los campos que el cliente mando excluyendo los otros
    for key, value in studio_data.dict(exclude_unset=True).items():
        setattr(studio,key,value)

    db.commit()
    db.refresh(studio)
    return studio

def delete_studio(db: Session, studio_id: int) -> Type[Studio] | None:
    # Busca el estudio con ese id
    studio = db.query(Studio).filter(Studio.id == studio_id).first()

    if not studio:
        return None

    # Lo borra y guarda los cambios en la bd
    db.delete(studio)
    db.commit()

    return studio

# EVENT ----------------------------------------------------------
def create_event(db: Session, event: EventCreate) -> Event | None:
    existing = db.query(Event).filter(Event.name == event.name).first()
    if existing:
        return None
    new_event = Event(**event.dict())
    db.add(new_event)
    db.commit()
    db.refresh(new_event)

    return new_event
def get_all_events(db: Session) -> list[Type[Event]]:
    return db.query(Event).all()

def get_event_by_name(db: Session, event_name: int) -> Optional[Event] | None:
    return db.query(Event).filter(Event.name == event_name).first()

def get_event_by_id(db: Session, event_id: int) -> Optional[Event] | None:
    return db.query(Event).filter(Event.id == event_id).first()

def update_event(db: Session, event_id: int, event_data:EventCreate) -> Type[Event] | None:
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        return None
    for key, value in event_data.dict(exclude_unset=True).items():
        setattr(event, key, value)

    db.commit()
    db.refresh(event)

    return event

def delete_event(db: Session, event_id: int) -> Type[Event] | None:
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        return None

    db.delete(event)
    db.commit()

    return event
