import modules.utils.core as core

if(__name__ == "__main__"):
    campus = {
        'campers': {}
    }

    core.MY_DATABASE = 'data/campus.json'

    core.checkFile(campus)

    # camper= {

    #     'idx' : str(len(campus.get('campers'))+1).zfill(3),
    #     'nombre' : 'Camper 1'
    # }

    # campus.get('campers').update({camper['idx']: camper})
    # core.addData(campus)



    
