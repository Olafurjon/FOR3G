if sek == spawntime:
readyfighters()
t0 = time.time()
t += 1
if t == 5:
    if k != 2:
        k += 1
    if k > 2:
        k == 2
    if k == 2:
        spawntime = 20

    t = 0

for tie in fighters:
    if tie.rect.x >= (resW - 30):
        print "snúavið"
        arg = "leftska"
        for tie in fighters:
            tie.move("down", int(k))

    if tie.rect.x <= 0:
        arg = "right"
        print "snúavið"
        for tie in fighters:
            tie.move("down", k)

for newtie in wave2:
    if newtie.rect.x >= (resW - 30):
        arg = "leftska"

    if newtie.rect.x <= 0:
        arg = "skaright"




for newtie in wave2:
    newtie.move(arg, int(k))
    if pygame.sprite.spritecollideany(newtie, clip):
        for bullet in clip:
            if bullet.rect.colliderect(newtie):
                all_sprites.remove(bullet)
                clip.remove(bullet)
        all_sprites.remove(newtie)
        wave2.remove(newtie)

