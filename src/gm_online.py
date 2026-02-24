from requests import Session

class GmOnline:
    def __init__(self) -> None:
        self.api = "https://f80c.playfabapi.com/Client"
        self.session = Session()
        self.session.headers = {
            "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 7.1.2; SM-G9880 Build/RP1A.2007201.012)",
            "X-PlayFabSdk": "UnitySDK-2.28.170925",
            "X-Unity-Version": "2019.1.6f1",
            "Content-Type": "application/json"
        }
        self.user_id = None
        self.title_id = "F80C"
        self.session_ticket = None
        
    def login(
            self,
            username: str,
            password: str) -> dict:
        data = {
            "Password": password,
            "TitleId": self.title_id,
            "Username": username
        }
        response = self.session.post(
            f"{self.api}/LoginWithPlayFab", json=data).json()
        if "SessionTicket" in response["data"]:
            self.user_id = response["data"]["PlayFabId"]
            self.session_ticket = response["data"]["SessionTicket"]
            self.session.headers["X-Authorization"] = self.session_ticket
        return response

    def register(
            self,
            username: str,
            password: str, 
            email: str) -> dict:
        data = {
            "DisplayName": username,
            "Email": email,
            "Password": password,
            "TitleId": self.title_id,
            "Username": username
        }
        return self.session.post(
            f"{self.api}/RegisterPlayFabUser", json=data).json()

    def get_account_info(self, username: str = None) -> dict:
        data = {
            "TitleDisplayName": username
        }
        return self.session.post(
            f"{self.api}/GetAccountInfo", json=data).json()

    def get_inventory(self) -> dict:        
        return self.session.post(
            f"{self.api}/GetUserInventory").json()

    def get_store_items(
            self,
            catalog_version: str = None,
            store_id: str = "Main Shop") -> dict:
        data = {
            "CatalogVersion": catalog_version,
            "StoreId": store_id
        }
        return self.session.post(
            f"{self.api}/GetStoreItems", json=data).json()

    def finish_video(self) -> dict:
        data = {
            "FunctionName": "FinishVideo",
            "FunctionParameter": {
                "id": 0,
            }
        }
        return self.session.post(
            f"{self.api}/ExecuteCloudScript", json=data).json()

    def update_username(self, username: str) -> dict:
        data = {
            "DisplayName": username
        }
        return self.session.post(
            f"{self.api}/UpdateUserTitleDisplayName", json=data).json()

    def get_friend_list(
            self,
            include_facebook_friends: bool = False,
            include_steam_friends: bool = False,
            show_statistics: bool = True,
            show_locations: bool = False,
            show_created: bool = True,
            show_last_login: bool = True,
            show_avatar_url: bool = True,
            show_banned_until: bool = True) -> dict:
        data = {
            "IncludeFacebookFriends": include_facebook_friends,
            "IncludeSteamFriends": include_steam_friends,
            "ProfileConstraints": {
                "ShowStatistics": show_statistics,
                "ShowLocations": show_locations,
                "ShowCreated": show_created,
                "ShowLastLogin": show_last_login,
                "ShowAvatarUrl": show_avatar_url,
                "ShowBannedUntil": show_banned_until
            }
        }
        return self.session.post(
            f"{self.api}/GetFriendsList", json=data).json()
    
    def send_friend_request(self, user_id: str, tag: str = "requested") -> dict:
        data = {
            "FunctionName": "SetFriendStatus",
            "FunctionParameter": {
                "id": self.user_id,
                "friendId": user_id,
                "tag": tag
            }
        }
        return self.session.post(
            f"{self.api}/ExecuteCloudScript", json=data).json()

    def cancel_friend_request(self, user_id: str) -> dict:
        data = {
            "FunctionName": "RemoveFriend",
            "FunctionParameter": {
                "friendId": user_id
            }
        }
        return self.session.post(
            f"{self.api}/ExecuteCloudScript", json=data).json()

    def get_player_profile(
            self,
            user_id: str,
            get_player_profile: bool = True,
            get_player_statistics: bool = True,
            get_user_account_info: bool = True,
            get_user_inventory: bool = True,
            get_user_data: bool = True,
            show_statistics: bool = True,
            show_locations: bool = True,
            show_created: bool = True,
            show_last_login: bool = True,
            show_avatar_url: bool = True,
            show_banned_until: bool = True,
            title_data_keys: list = ["ConsumedDeals", "Referrals"]) -> dict:
        data = {
            "FunctionName": "GetPlayerProfile",
            "FunctionParameter": {
                "request": {
                    "InfoRequestParameters": {
                        "GetPlayerProfile": get_player_profile,
                        "GetPlayerStatistics": get_player_statistics,
                        "GetUserAccountInfo": get_user_account_info,
                        "GetUserInventory": get_user_inventory,
                        "GetUserData": get_user_data,
                        "ProfileConstraints": {
                            "ShowStatistics": show_statistics,
                            "ShowLocations": show_locations,
                            "ShowCreated": show_created,
                            "ShowLastLogin": show_last_login,
                            "ShowAvatarUrl": show_avatar_url,
                            "ShowBannedUntil": show_banned_until
                        },
                        "TitleDataKeys": title_data_keys,
                    },
                    "PlayFabId": user_id
                }
            }
        }
        return self.session.post(
            f"{self.api}/ExecuteCloudScript", json=data).json()

    def purchase_item(
            self, 
            item_id: str, 
            price: int, 
            virtual_currency: str,
            catalog_version: str = None,
            character_id: str = None,
            store_id: str = "Main Shop") -> dict:
        data = {
            "CatalogVersion": catalog_version,
            "CharacterId": character_id,
            "itemId": item_id,
            "Price": price,
            "StoreId": store_id,
            "VirtualCurrency": virtual_currency
        }
        return self.session.post(
            f"{self.api}/PurchaseItem", json=data).json()

    def unlock_container_instance(
            self,
            item_instance_id: str,
            catalog_version: str = None,
            character_id: str = None,
            key_item_instance_id: str = None) -> dict:
        data = {
            "CatalogVersion": catalog_version,
            "CharacterId": character_id,
            "ContainerItemInstanceId": item_instance_id,
            "KeyItemInstanceId": key_item_instance_id
        }
        return self.session.post(
            f"{self.api}/UnlockContainerInstance", json=data).json()

    def finish_game(
            self,
            game: str, 
            status: str) -> dict:
        data = {
            "FunctionName": "FinishGame",
            "FunctionParameter": {
                "game": game,
                "status": status
            }
        }
        return self.session.post(
            f"{self.api}/ExecuteCloudScript", json=data).json()

    def add_played_time(self, game: str) -> dict:
        data = {
            "FunctionName": "AddPlayedTime",
            "FunctionParameter": {
                "game": game
            }
        }
        return self.session.post(
            f"{self.api}/ExecuteCloudScript", json=data).json()

    def update_avatar_url(self, image_url: str) -> dict:
        data = {"ImageUrl": image_url}
        return self.session.post(
            f"{self.api}/UpdateAvatarUrl", json=data).json()

    def send_account_recovery_mail(self, email: str) -> dict:
        data = {
            "Email": email,
            "TitleId": self.title_id
        }
        return self.session.post(
            f"{self.api}/SendAccountRecoveryEmail", json=data).json()
    
    def craft_items(self, items: list, bundle: list = ["0000"]) -> dict:
        data = {
            "FunctionName": "craftItems",
            "FunctionParameter": {
                "items": items,
                "bundle": bundle
            }
        }
        return self.session.post(
            f"{self.api}/ExecuteCloudScript", json=data).json()
    
    def get_catalog_items(
            self,
            catalog_version: str = "Main") -> dict:
        data = {
            "Catalog Version": catalog_version
        }
        return self.session.post(
            f"{self.api}/GetCatalogItems", json=data).json()
        
    def update_email(self, email: str) -> dict:
        data = {
            "EmailAddress": email
        }
        return self.session.post(
            f"{self.api}/AddOrUpdateContactEmail", json=data).json()
