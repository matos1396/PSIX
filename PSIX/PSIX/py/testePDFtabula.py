import tabula



#testtabula = tabula.read_pdf("C:/Users/Gustavo Matos/Downloads/CADASTRO_TURMAS_20202.pdf", pages = 'all', stream=True)

testtabula2 = tabula.convert_into("CADASTRO_TURMAS_20202.pdf", "output.csv", output_format="csv", pages='all')