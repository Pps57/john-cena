
def on_a_pressed():
    global projectile
    projectile = sprites.create_projectile_from_sprite(assets.image("""
        arrow
    """), slug, 500, 0)
    pause(2000)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite, otherSprite):
    animation.run_image_animation(player_2, assets.animation("""
        12
    """), 500, False)
    info.player2.change_life_by(-1)
    pause(5000)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.player, on_on_overlap)

def on_on_overlap2(sprite2, otherSprite2):
    info.player2.change_life_by(1)
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap2)

projectile: Sprite = None
slug: Sprite = None
player_2: Sprite = None
scene.set_background_image(assets.image("""
    fight scene
"""))
player_2 = sprites.create(assets.image("""
    player 2
"""), SpriteKind.player)
controller.player2.move_sprite(player_2, 50, 50)
info.player2.set_life(3)
slug = sprites.create(assets.image("""
    hi
"""), SpriteKind.player)
controller.move_sprite(slug)
info.player1.set_life(3)
player_2.set_stay_in_screen(True)
slug.set_stay_in_screen(True)
pizza = sprites.create(img("""
        .............beebbbb............................................
            ............eebbbb4bb...........................................
            ............eb344bb4bb..........................................
            ............e44334bb4bb.........................................
            ............eb433344b4be........................................
            ............4eb43344444be.......................................
            ...........bd4eb43333344bb......................................
            ..........b455d4443333444bb.....................................
            ..........4d5555d444333444bb....................................
            .........4555555dd4b4443444be...................................
            ........bd5555d555d4bb444444ee..................................
            ........b55ddd665555bb4b44444ee.................................
            .......bd5555677655554ebb44444eb................................
            .......43222558855555d4eeb44b4ee................................
            ......b422332ddd555222d4eebbb4be................................
            ......be22232ed55522332db4ebbbbe................................
            .....bde22222e555e22232edd4bbbbe................................
            .....b52e222e3555e22222eddd4ebee................................
            ....bd552eee355552e222e355544eee................................
            ....665dd5555555552eee355dd4deee................................
            ...6776555555555555555551554d4ee................................
            ...4885222555dddd6655551544d4eee................................
            ..b45522332555dd677611d444ddeee.................................
            ..4d5222232e55555881d44ddd4eee..................................
            .bdd5e22222e555115114d54d4ee....................................
            .b55d2e222e351144d1d55eeee......................................
            bd5ddd2eee3d444555dd4e..........................................
            b555115dddd55d544eede...........................................
            4511d444d5544ee...4de...........................................
            41d4555d4ee........44...........................................
            41554eede.......................................................
            44ee...4e.......................................................
            ................................................................
            ................................................................
            ................................................................
            ................................................................
            ................................................................
            ................................................................
            ................................................................
            ................................................................
            ................................................................
            ................................................................
            ................................................................
            ................................................................
            ................................................................
            ................................................................
            ................................................................
            ................................................................
            ................................................................
            ................................................................
            ................................................................
            ................................................................
            ................................................................
            ................................................................
            ................................................................
            ................................................................
            ................................................................
            ................................................................
            ................................................................
            ................................................................
            ................................................................
            ................................................................
            ................................................................
            ................................................................
    """),
    SpriteKind.food)
tiles.place_on_random_tile(pizza, assets.tile("""
    transparency16
"""))
music.set_volume(20)