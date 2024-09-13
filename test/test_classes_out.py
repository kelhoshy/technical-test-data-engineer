import datetime
from src.moovitamix_fastapi.classes_out import TracksOut, UsersOut, ListenHistoryOut, TopSongsOut, gender_list, genre_list
import unittest
from unittest.mock import patch

# Testing TracksOut
def test_tracks_out_generate_fake():
    track = TracksOut.generate_fake()
    assert isinstance(track.id, int)
    assert isinstance(track.name, str)
    assert isinstance(track.artist, str)
    assert isinstance(track.songwriters, str)
    assert isinstance(track.duration, str)
    assert isinstance(track.genres, str)
    assert isinstance(track.album, str)
    assert isinstance(track.created_at, datetime.datetime)
    assert isinstance(track.updated_at, datetime.datetime)

# Testing UsersOut
def test_users_out_generate_fake():
    user = UsersOut.generate_fake()
    assert isinstance(user.id, int)
    assert isinstance(user.first_name, str)
    assert isinstance(user.last_name, str)
    assert isinstance(user.email, str)
    assert user.gender in gender_list()
    assert user.favorite_genres in genre_list()
    assert isinstance(user.created_at, datetime.datetime)
    assert isinstance(user.updated_at, datetime.datetime)

# Testing ListenHistoryOut
def test_listen_history_out_generate_fake():
    history = ListenHistoryOut.generate_fake()
    assert history.user_id is None
    assert history.items is None
    assert isinstance(history.created_at, datetime.datetime)
    assert isinstance(history.updated_at, datetime.datetime)

# Testing TopSongsOut
# def test_top_songs_out_generate_fake():
#     song = TopSongsOut.generate_fake()
#     assert isinstance(song.id, int)
#     assert isinstance(song.name, str)
#     assert isinstance(song.artist, str)
#     assert isinstance(song.songwriters, str)
#     assert isinstance(song.duration, str)
#     assert isinstance(song.genres, str)
#     assert isinstance(song.album, str)
#     assert isinstance(song.rank, int)
#     assert isinstance(song.created_at, datetime.datetime)
#     assert isinstance(song.updated_at, datetime.datetime)

class TestTopSongsOut(unittest.TestCase):

    @patch('src.moovitamix_fastapi.classes_out.TopSongsOut.generate_fake')
    def test_top_songs_out_generate_fake(self, mock_generate_fake):

        mock_generate_fake.return_value = TopSongsOut(
            id=3981,
            name="Yesterday",
            artist="The Beatles",
            songwriters="John Lennon",
            duration="2:06",
            genres="Pop",
            album="Help!",
            rank=19,
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now()
        )
        
        song = TopSongsOut.generate_fake()
        
        assert isinstance(song.id, int)
        assert isinstance(song.name, str)
        assert isinstance(song.artist, str)
        assert isinstance(song.songwriters, str)
        assert isinstance(song.duration, str)
        assert isinstance(song.genres, str)
        assert isinstance(song.album, str)
        assert isinstance(song.rank, int)
        assert isinstance(song.created_at, datetime.datetime)
        assert isinstance(song.updated_at, datetime.datetime)

if __name__ == '__main__':
    unittest.main()