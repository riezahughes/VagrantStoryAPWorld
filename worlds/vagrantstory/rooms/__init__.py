from . import abandoned_mines_b1
from . import abandoned_mines_b2
from . import catacombs
from . import city_walls_east
from . import city_walls_north
from . import city_walls_south
from . import city_walls_west
from . import escapeway
from . import forgotten_pathway
from . import great_cathedral_B1
from . import great_cathedral_L1
from . import great_cathedral_L2
from . import great_cathedral_L3
from . import great_cathedral_L4
from . import great_cathedral_dome
from . import iron_maiden_b1
from . import iron_maiden_b2
from . import iron_maiden_b3
from . import limestone_quarry
from . import sanctum
from . import snowfly_forest_east
from . import snowfly_forest
from . import temple_of_kiltia
from . import the_keep
from . import town_centre_east
from . import town_centre_south
from . import town_centre_west
from . import undercity_east
from . import undercity_west
from . import wine_cellar

all_major_regions = {
    "wine_cellar": wine_cellar.room_data,
    "undercity_west": undercity_west.room_data,
    "undercity_east": undercity_east.room_data,
    "town_centre_south": town_centre_south.room_data,
    "town_centre_east": town_centre_east.room_data,
    "town_centre_west": town_centre_west.room_data,
    "the_keep": the_keep.room_data,
    "temple_of_kiltia": temple_of_kiltia.room_data,
    "snowfly_forest": snowfly_forest.room_data,
    "snowfly_forest_east": snowfly_forest_east.room_data,
    "sanctum": sanctum.room_data,
    "limestone_quarry": limestone_quarry.room_data,
    "iron_maiden_b1": iron_maiden_b1.room_data,
    "iron_miden_b2": iron_maiden_b2.room_data,
    "iron_miden_b3": iron_maiden_b3.room_data,
    "great_cathedral_L1": great_cathedral_L1.room_data,
    "great_cathedral_B1": great_cathedral_B1.room_data,
    "great_cathedral_L2": great_cathedral_L2.room_data,
    "great_cathedral_L3": great_cathedral_L3.room_data,
    "great_cathedral_L4": great_cathedral_L4.room_data,
    "great_cathedral_dome": great_cathedral_dome.room_data,
    "forgotten_pathway": forgotten_pathway.room_data,
    "escapeway": escapeway.room_data,
    "city_walls_west": city_walls_west.room_data,
    "city_walls_south": city_walls_south.room_data,
    "city_walls_north": city_walls_north.room_data,
    "city_walls_east": city_walls_east.room_data,
    "catacombs": catacombs.room_data,
    "abandoned_mines_b1": abandoned_mines_b1.room_data,
    "abandoned_mines_b2": abandoned_mines_b2.room_data,
}

all_minor_regions = {room_name: data for region_dict in all_major_regions.values() for room_name, data in region_dict.items()}
