import fitbit
unauth_client = fitbit.Fitbit('227NXZ', 'b9d240939f4d944e93bb4ec5eed00b49')
# certain methods do not require user keys
unauth_client.food_units()