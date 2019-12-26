import discord
from discord.ext import commands
import random
import asyncio

TOKEN = 'YOURTOKEN'

prefix = '+'

bot = commands.Bot(command_prefix=prefix)
client = discord.Client()


#newEvents
tmpEventMsgID = 00

eventJoinners=[]
eventCaptains=[]
eventNotPlaying=[]

captainValue = "Personne."
memberValue = "Personne."
notMemberValue = "Personne."


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    
@bot.event
async def on_raw_reaction_add(payload):
    global captainValue, memberValue, notMemberValue, tmpEventMsgID, eventCaptains, eventJoinners, eventNotPlaying
    guild = bot.get_guild(payload.guild_id)
    channel = bot.get_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)
    user = bot.get_user(payload.user_id)
    member = guild.get_member(payload.user_id)
    
    if user != bot.user:        
        if payload.message_id == 645462083735126077: #write msg id
            global tmpRole
            
            if str(payload.emoji) == "🏴":
                tmpRoleID = 604658715609530379 #write id w/o @& pirates
                    
            if str(payload.emoji) == "⚓":
                tmpRoleID = 605093465847627838 #write id w/o @& matelos
                    
            if str(payload.emoji) == "💰":
                tmpRoleID = 644568722668781608 #write id w/o @& chercheurs d'or
                    
            if str(payload.emoji) == "🐍":
                tmpRoleID = 644569405598203917 #write id w/o @& aventuriers
                    
            if str(payload.emoji) == "🎣":
                tmpRoleID = 644568768844136478 #write id w/o @& pecheurs
                    
            if str(payload.emoji) == "🐬":
                tmpRoleID = 644570037876686850 #write id w/o @& espadons
                    
            if str(payload.emoji) == "💀":
                tmpRoleID = 597378562051407908 #write id w/o @& legendes
                    
            if str(payload.emoji) == "🥁":
                tmpRoleID = 607628787823149081 #write id w/o @& troubadours
               
            if str(payload.emoji) == "🧙‍♂️":
                tmpRoleID = 616643229713957076 #write id w/o @& jambes de bois
                    
            if str(payload.emoji) == "🚧":
                tmpRoleID = 597378766997815316 #write id w/o @& insiders
                        
                    
            tmpRole = guild.get_role(tmpRoleID)
            await member.add_roles(tmpRole)
            print(member.name + ' est devenu un ' + tmpRole.name + '!')
            await dmAddRoleFeedback(user, tmpRole.name)
            
            
        if payload.message_id == 647226168151638057:  
            tmpRoleID = 646084429885734934 #write id w/o @& membres de la flotte
            
            tmpRole = guild.get_role(tmpRoleID)
            await member.add_roles(tmpRole)
            print(member.name + ' a rejoint les ' + tmpRole.name + '!')
            await dmAddRoleFeedback(user, tmpRole.name)
            
            
        if payload.message_id == eventMsg.id: #write msg id
            if tmpEventMsgID != eventMsg.id:
                eventJoinners=[]
                eventCaptains=[]
                eventNotPlaying=[]
            
            tmpEventMsgID = eventMsg.id
            mRoles = []
            
            if str(payload.emoji) == "✅":
                if member.name in eventNotPlaying:
                    await eventMsg.remove_reaction("❌", member)
                    
                for role in member.roles:
                    mRoles.append(role.name)
                    
                if "Capitaines" in mRoles:
                    eventCaptains.append(member.name)
                    print ("eventCaptains :")
                    print (eventCaptains)
                    
                    if len(eventCaptains) == 0:
                        captainValue = "Personne."
                    else:
                        for i in range(len(eventCaptains)):
                            if i == (len(eventCaptains)-1):
                                if i == 0:
                                    captainValue = ("\n" + eventCaptains[i] + ".")
                                    
                                else:
                                    captainValue += ("\n" + eventCaptains[i] + ".")
                                
                            elif i == 0:
                                captainValue = (eventCaptains[i] + ",")
                                
                            else:
                                captainValue += ("\n" + eventCaptains[i] + ",")
                        
                else:
                    eventJoinners.append(member.name)
                    print ("eventJoinners :")
                    print (eventJoinners)
                    
                    if len(eventJoinners) == 0:
                        memberValue = "Personne."
                    else:
                        for i in range(len(eventJoinners)):
                            if i == (len(eventJoinners)-1):
                                if i == 0:
                                    memberValue = ("\n" + eventJoinners[i] + ".")
                                    
                                else:
                                    memberValue += ("\n" + eventJoinners[i] + ".")
                                
                            elif i == 0:
                                memberValue = (eventJoinners[i] + ",")
                                
                            else:
                                memberValue += ("\n" + eventJoinners[i] + ",")
            
            if str(payload.emoji) == "❌":
                if member.name in eventCaptains:
                    await eventMsg.remove_reaction("✅", member)
                    
                if member.name in eventJoinners:
                    await eventMsg.remove_reaction("✅", member)
                    
                eventNotPlaying.append(member.name)
                print ("eventNotPlaying :")
                print (eventNotPlaying)
                
                if len(eventNotPlaying) == 0:
                    notMemberValue = "Personne."
                else:
                    for i in range(len(eventNotPlaying)):
                        if i == (len(eventNotPlaying)-1):
                            if i == 0:
                                notMemberValue = ("\n" + eventNotPlaying[i] + ".")
                                
                            else:
                                notMemberValue += ("\n" + eventNotPlaying[i] + ".")
                            
                        elif i == 0:
                            notMemberValue = (eventNotPlaying[i] + ",")
                            
                        else:
                            notMemberValue += ("\n" + eventNotPlaying[i] + ",")
                
            embedEvent = discord.Embed(title = "Appel aux armes!", color=0xff0000)
        
            embedEvent.add_field(name = "Membres :", value = memberValue, inline= True)
            embedEvent.add_field(name = "Capitaines :", value = captainValue, inline= True)
            embedEvent.add_field(name = "Non-participants :", value = notMemberValue, inline= True)

            embedEvent.set_footer(text = "✅ pour répondre à l'appel, ❌ pour renoncer à cette aventure")
            
            await eventMsg.edit(embed=embedEvent)
            
    else:
        print ("Coucou c'est moi le bot!")
    
        
        
async def dmAddRoleFeedback(user, role):
    if role == "Membres de la flotte":
        await user.send("Tu viens de rejoindre les " + role + "!")
        
    else:
        await user.send("Hum... Tu fais parti des " + role)
    

@bot.event
async def on_raw_reaction_remove(payload):
    global captainValue, memberValue, notMemberValue, tmpEventMsgID, eventCaptains, eventJoinners, eventNotPlaying
    guild = bot.get_guild(payload.guild_id)
    channel = bot.get_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)
    user = bot.get_user(payload.user_id)
    member = guild.get_member(payload.user_id)
    
    if user != bot.user:    
        if payload.message_id == 645462083735126077: #write msg id
            global tmpRole
            
            if str(payload.emoji) == "🏴":
                tmpRoleID = 604658715609530379 #write id w/o @& pirates
                    
            if str(payload.emoji) == "⚓":
                tmpRoleID = 605093465847627838 #write id w/o @& matelos
                    
            if str(payload.emoji) == "💰":
                tmpRoleID = 644568722668781608 #write id w/o @& chercheurs d'or
                    
            if str(payload.emoji) == "🐍":
                tmpRoleID = 644569405598203917 #write id w/o @& aventuriers
                    
            if str(payload.emoji) == "🎣":
                tmpRoleID = 644568768844136478 #write id w/o @& pecheurs
                    
            if str(payload.emoji) == "🐬":
                tmpRoleID = 644570037876686850 #write id w/o @& espadons
                    
            if str(payload.emoji) == "💀":
                tmpRoleID = 597378562051407908 #write id w/o @& legendes
                    
            if str(payload.emoji) == "🥁":
                tmpRoleID = 607628787823149081 #write id w/o @& troubadours
               
            if str(payload.emoji) == "🧙‍♂️":
                tmpRoleID = 616643229713957076 #write id w/o @& jambes de bois
                    
            if str(payload.emoji) == "🚧":
                tmpRoleID = 597378766997815316 #write id w/o @& insiders
                    
                
            tmpRole = guild.get_role(tmpRoleID)
            await member.remove_roles(tmpRole)
            print(member.name + " n'est plus un " + tmpRole.name + "!")
            await dmRemoveRoleFeedback(user, tmpRole.name)
            
        if payload.message_id == 647226168151638057:  
            tmpRoleID = 646084429885734934 #write id w/o @& membres de la flotte
            
            tmpRole = guild.get_role(tmpRoleID)
            await member.remove_roles(tmpRole)
            print(member.name + " a quitté " + tmpRole.name + "!")
            await dmRemoveRoleFeedback(user, tmpRole.name)
            
        if payload.message_id == eventMsg.id: #write msg id
            if tmpEventMsgID != eventMsg.id:
                eventJoinners=[]
                eventCaptains=[]
                eventNotPlaying=[]
                
            tmpEventMsgID != eventMsg.id
            mRoles = []
            
            if str(payload.emoji) == "✅":
                for role in member.roles:
                    mRoles.append(role.name)
                    
                if "Capitaines" in mRoles:
                    eventCaptains.remove(member.name)
                    print ("eventCaptains :")
                    print (eventCaptains)
                    
                    if len(eventCaptains) == 0:
                        captainValue = "Personne."
                    else:
                        for i in range(len(eventCaptains)):
                            if i == (len(eventCaptains)-1):
                                if i == 0:
                                    captainValue = ("\n" + eventCaptains[i] + ".")
                                    
                                else:
                                    captainValue += ("\n" + eventCaptains[i] + ".")
                                
                            elif i == 0:
                                captainValue = (eventCaptains[i] + ",")
                                
                            else:
                                captainValue += ("\n" + eventCaptains[i] + ",")
                        
                else:
                    eventJoinners.remove(member.name)
                    print ("eventJoinners :")
                    print (eventJoinners)
                    
                    if len(eventJoinners) == 0:
                        memberValue = "Personne."
                    else:
                        for i in range(len(eventJoinners)):
                            if i == (len(eventJoinners)-1):
                                if i == 0:
                                    memberValue = ("\n" + eventJoinners[i] + ".")
                                    
                                else:
                                    memberValue += ("\n" + eventJoinners[i] + ".")
                                
                            elif i == 0:
                                memberValue = (eventJoinners[i] + ",")
                                
                            else:
                                memberValue += ("\n" + eventJoinners[i] + ",")
            
            if str(payload.emoji) == "❌":
                eventNotPlaying.remove(member.name)
                print ("eventNotPlaying :")
                print (eventNotPlaying)
                
                if len(eventNotPlaying) == 0:
                    notMemberValue = "Personne."
                else:
                    for i in range(len(eventNotPlaying)):
                        if i == (len(eventNotPlaying)-1):
                            if i == 0:
                                notMemberValue = ("\n" + eventNotPlaying[i] + ".")
                                
                            else:
                                notMemberValue += ("\n" + eventNotPlaying[i] + ".")
                            
                        elif i == 0:
                            notMemberValue = (eventNotPlaying[i] + ",")
                            
                        else:
                            notMemberValue += ("\n" + eventNotPlaying[i] + ",")
                
            embedEvent = discord.Embed(title = "Appel aux armes!", color=0xff0000)
        
            embedEvent.add_field(name = "Membres :", value = memberValue, inline= True)
            embedEvent.add_field(name = "Capitaines :", value = captainValue, inline= True)
            embedEvent.add_field(name = "Non-participants :", value = notMemberValue, inline= True)

            embedEvent.set_footer(text = "✅ pour répondre à l'appel, ❌ pour renoncer à cette aventure")
            
            await eventMsg.edit(embed=embedEvent)
            
    else:
        print ("Coucou c'est moi le bot!")
        
        
async def dmRemoveRoleFeedback(user, role):
    if role == "Membres de la flotte":
        await user.send("Tu a quitté les " + role + "...")
    else:
        await user.send("Tu n'es plus membre des " + role + "?")
    
@bot.command()
async def roleSetup(ctx):
    if ctx.author == ctx.guild.owner:
        await ctx.message.channel.purge()
        
        reactionsEmojis = ["🏴", "⚓", "💰", "🐍", "🎣", "🐬", "💀", "🥁", "🧙‍♂️", "🚧"]
        newMsg = await ctx.send("Alors pirate, quelle est ta vrai nature?\nLe Pirate 🏴 est reconnu de tous comme le guerrier le plus sanguinaire des mers, toujours partant pour aborder n'importe quel navire!\nLe Matelos ⚓,lui, est plus détendu. Il n'est pas là pour se faire des ennemis... Mais attention! Ca ne veut pas dire qu'il ne sait pas se battre!\nLe chercheur d'or 💰, probablement le plus populaire! Seulement l'OR compte à ses yeux, il serait prêt à trahir pour avoir son butin...\nL'aventurier 🐍... Toujours à vouloir découvrir les secrets les plus enfouis de ce monde!\nAh mon préféré, le pêcheur 🎣! Gentil, amical, amoureux de la pêche et de la mer mais faites attention à ne pas le mettre de mauvaise humeur ou vous risqueriez de tous perdre!\nL'espadon 🐬, un seul objectif! Etre le plus connu auprès des différentes sociétés!\nLa légende pirate 💀, faites-vous un nom et revenez me voir...\nToujours là pour mettre l'ambiance ces troubadours 🥁!\n'Pas besoin d'aller en mer quand on a de l'imagination' est la devise des autoproclamés 'Jambes de bois 🧙‍♂'.\nVous etes membre des Insiders 🚧? Voici votre laissez passer.\nRéagis en fonction de qui tu es vraiment...\n[...]")
        for emoji in reactionsEmojis:
            await newMsg.add_reaction(emoji)
                
@bot.command()
async def welcomeSetup(ctx):
    if ctx.author == ctx.guild.owner:
        await ctx.message.channel.purge()
        
        chnlRoleID = 597415175796293662
        chnlRole = bot.get_channel(chnlRoleID)
        reactionsEmojis = ["⚓", "🍌", "🍍", "🥥", "💀", "🎣"]
        newMsg = await ctx.send("Bonjour, pirate.\n[...]\nLe seigneur de la piraterie vous invite à rejoindre son équipage secret.\nJ'espère que vous serez à la hauteur si vous ne voulez pas vous retrouver coincé à jamais dans le monde des morts...\n[...]\nUne dernière étape avant de pouvoir le rejoindre.\nDirige toi vers " + chnlRole.mention + " pour nous avouer ta vrai nature!\n[...]\nUn instant! Si tu connais des pirates dignes de faire partie de cette escouade, dis le moi et j'en toucherai un mot au patron.\n https://discord.gg/SnEmTVd \n[...]\nNe nous déçoit pas!")
        for emoji in reactionsEmojis:
            await newMsg.add_reaction(emoji)


@bot.command()
async def creatEvent(ctx):
    msgAuthor = ctx.author
    global eventMsg
    
    eventJoinners=[]
    eventCaptains=[]
    eventNotPlaying=[]
    
    captainValue = "Personne."
    memberValue = "Personne."
    notMemberValue = "Personne."
    
    eventCaptains.append(msgAuthor.name)
    
    embedEvent = discord.Embed(title = "Appel aux armes!", color=0xff0000)
    
    embedEvent.add_field(name = "Membres :", value = memberValue, inline= True)
    embedEvent.add_field(name = "Capitaines :", value = captainValue, inline= True)
    embedEvent.add_field(name = "Non-participants :", value = notMemberValue, inline= True)
    
    embedEvent.set_footer(text = "✅ pour répondre à l'appel, ❌ pour renoncer à cette aventure")
    
    eventMsg = await ctx.send(str(ctx.guild.default_role) + " - " + msgAuthor.mention + " demande a la flotte de Mitch l'impitoyable de se rassembler une fois de plus pour braver l'inconnu et dominer la mer des voleurs!", embed = embedEvent)
    
    reactionsEmojis = ["✅", "❌"]
    for emoji in reactionsEmojis:
        await eventMsg.add_reaction(emoji)

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="Un mystérieux étranger, un bot 'LES'", description="Calme et intrigant...", color=0x04fdf3)

    # Shows the number of servers the bot is member of.
    embed.add_field(name="Histoire :", value="Missionné par le Seigneur de la piraterie en personne pour parcourir les tavernes du monde entier afin d'inviter les pirates les plus 'cool' que la mer des voleurs n'est jamais connu à rejoindre l'escouade secrete : L'écaille scintillante...")

    # give users a link to invite thsi bot to their server
    embed.add_field(name="Pirates cool : ", value=len(bot.guilds.members))
    
    # give info about you here
    embed.add_field(name="Crédit :", value="Bot design : Papsi#1809\nBot dev : Papsi#1809\nBot host : Eklips#3553 & Papsi#1809")

    await ctx.send(embed=embed)

bot.run(TOKEN)  # Where 'TOKEN' is your bot token
