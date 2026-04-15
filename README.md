# <img src="https://play-lh.googleusercontent.com/haYSjrpLxxHY65cAQzk-BKSpZwoiyemHN0CSjPp4hkHBKZacFQiYm0hnJh9pnG_8MUNnHvMFJ1YeGfrJLbPwRLo=w240-h480-rw" width="28" style="vertical-align:middle;" /> gm_online.py

> Mobile-API for [GM Online](https://play.google.com/store/apps/details?id=com.CGD.MGC) a mobile game built on [PlayFab](https://playfab.com).

## Quick Start

```python
from gm_online import GmOnline

gm = GmOnline()
gm.login(username="Hero", password="secret")
```

## Usage

### Authentication

```python
# Login
gm.login(username="Hero", password="secret")

# Register
gm.register(username="Hero", password="secret", email="you@example.com")

# Recover password
gm.send_account_recovery_mail(email="you@example.com")
```

### Player

```python
gm.get_account_info()
gm.get_player_profile(user_id="ABC123")
gm.update_username("NewName")
gm.update_avatar_url("https://example.com/avatar.jpg")
gm.update_email("new@example.com")
```

### Inventory & Store

```python
gm.get_inventory()
gm.get_catalog_items()
gm.get_store_items(store_id="Main Shop")
gm.purchase_item(item_id="sword_01", price=100, virtual_currency="GM")
gm.unlock_container_instance(item_instance_id="inst_123")
gm.craft_items(items=["item_01", "item_02"])
```

### Friends

```python
gm.get_friend_list()
gm.send_friend_request(user_id="ABC123")
gm.cancel_friend_request(user_id="ABC123")
```

### gms

```python
# Finish a gm session
gm.finish_gm(gm="poker", status="win")

# Track playtime
gm.add_played_time(gm="poker")

# Finish watching a video ad
gm.finish_video()
```

## API Reference

| Method | Description |
|---|---|
| `login(username, password)` | Login to your account |
| `register(username, password, email)` | Register a new account |
| `send_account_recovery_mail(email)` | Send a password recovery email |
| `get_account_info(username)` | Get account info |
| `get_player_profile(user_id)` | Get a player's full profile |
| `update_username(username)` | Update display name |
| `update_avatar_url(image_url)` | Update avatar |
| `update_email(email)` | Update contact email |
| `get_inventory()` | Get your inventory |
| `get_catalog_items()` | Get all catalog items |
| `get_store_items(store_id)` | Get store listings |
| `purchase_item(item_id, price, virtual_currency)` | Buy an item |
| `unlock_container_instance(item_instance_id)` | Open a container |
| `craft_items(items)` | Craft items |
| `get_friend_list()` | Get friends list |
| `send_friend_request(user_id)` | Send a friend request |
| `cancel_friend_request(user_id)` | Remove a friend |
| `finish_gm(gm, status)` | Submit a gm result |
| `add_played_time(gm)` | Track playtime |
| `finish_video()` | Claim video ad reward |
