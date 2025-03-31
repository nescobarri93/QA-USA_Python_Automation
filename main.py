import data
import helpers

class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Connected to the Urban Routes server")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running")

    def test_set_route(self):
        # todo S8
        pass

    def test_select_plan(self):
        # todo S8
        pass

    def test_fill_phone_number(self):
        # todo S8
        pass

    def test_fill_card(self):
        # todo S8
        pass

    def test_comment_for_driver(self):
        # todo S8
        pass

    def test_order_blanket_and_handkerchiefs(self):
        # todo S8
        pass

    def test_order_2_ice_creams(self):
        number_of_ice_creams = 2
        for count in range(number_of_ice_creams):
            # todo S8
            pass

    def test_car_search_model_appears(self):
        # todo S8
        pass


''' #deprecated
    def test_driver_info_appears(self):
        # todo S8
        pass

        print('hello')
'''
