import unittest
from unittest.mock import patch, MagicMock
from downloader import baixar_video  # supondo que sua função esteja no arquivo downloader.py


class TestDownloader(unittest.TestCase):
    @patch("downloader.YouTube")
    def test_baixar_video_sucesso(self, mock_youtube):
        # Simula o objeto YouTube e o stream
        mock_stream = MagicMock()
        mock_stream.download.return_value = None
        
        mock_youtube.return_value.streams.get_highest_resolution.return_value = mock_stream
        
        # Executa a função
        resultado = baixar_video("https://youtube.com/fakevideo", "downloads/")
        
        # Verifica se o método download foi chamado
        mock_stream.download.assert_called_once_with("downloads/")
        self.assertEqual(resultado, "Download concluído com sucesso!")

    @patch("downloader.YouTube")
    def test_baixar_video_erro(self, mock_youtube):
        # Simula erro ao criar o objeto YouTube
        mock_youtube.side_effect = Exception("Erro no YouTube")
        
        resultado = baixar_video("https://youtube.com/fakevideo", "downloads/")
        
        # Verifica se retorna a mensagem de erro
        self.assertIn("Erro ao baixar vídeo", resultado)


if __name__ == "__main__":
    unittest.main()
