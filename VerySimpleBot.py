import discord
from discord.ext import commands
from urllib import parse, request
import random
import re

#6/09/22 Este es el primer codigo que subo aqui, este es un bot muy sencillo creado enteramente por mi, funcional con las versiones de python que usen discord.py
#posee funciones como 8ball,Joke,youtube(para ver videos de youtube),para moderar de forma bastante sencilla nuestro servidor.
#espero que les sirva. muchas gracias.
#----------Variable Principal-----------------

bot = commands.Bot(command_prefix='.')

#----------Comandos Sencillos-----------------

@bot.command()
async def hola(ctx):
	await ctx.send('que tal :3')

@bot.command()
async def ping(ctx):
	await ctx.send('pong')

@bot.command()
async def info(ctx):
	await ctx.send('Version 1.0 "VerySimpleBot" \n Bot completamente creado en Python 3 y Discord.py \n Escribe "comandos" para saber la lista de comandos disponibles para esta version.')

@bot.command()
async def comandos(ctx):
	await ctx.send('La Lista de comandos es: \n_"info": Informacion del Bot. \n_"youtube": Comando de busqueda de videos en youtube. \n _Comandos de MOD_ \n_"kick": hecha a un miembro del servidor (no lo banea) \n_"ban": baneo al usuario \n_"forgive": desbaneo de usuario \n_"clear": limpia el canal de texto donde es ejecutado (¡¡OJO!! = hasta 100 mensajes) \n_"bolaocho": hazle una pregunta, la respuesta te sorprendera. \n_"chiste": el bot cuenta un chiste. \n >> Recuerda crear un rol con permisos de "Administrador" para el funcionamiento optimo del bot <<')

@bot.command()
async def youtube(ctx,*,search):
	query_string = parse.urlencode({'search_query':search})
	html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
	search_results = re.findall(r"watch\?v=(\S{11})", html_content.read().decode())
	await ctx.send('https://www.youtube.com/watch?v='+ search_results[0])

#----------Comandos De Moderacion-------------

@bot.command(aliases=['boot'])
async def kick(ctx,member:discord.Member,*,reason=None):
	await member.kick(reason=reason)
	await ctx.send(f'{member.mention} ha sido expulsado')

@bot.command(aliases=['hammer'])
async def ban(ctx,member:discord.Member,*,reason=None):
	await member.ban(reason=reason)
	await ctx.send(f'{member.mention} ha sido baneado')

@bot.command(aliases=['forgive'])
async def unban(ctx,*,member):
	banned_users = await ctx.guild.bans()
	member_name,member_discriminator = member.split("#")

	for ban_entry in banned_users:
		user = ban_entry.user

		if(user.name, user.discriminator)==(member_name,member_discriminator):
			await ctx.guild.unban(user)
			await ctx.send(f'{user.mention} Ha sido desbaneado')
			return
			
@bot.command(aliases=['purge'])
async def clear(ctx,amount=11):
	ammount = amount+1
	if amount > 101:
		await ctx.send('No puedo eliminar mas de 100 mensajes (´･_･`)')
	else:
		await ctx.channel.purge(limit=amount)
		await ctx.send('Mensajes eliminados Satisfactoriamente :D')

#----------Comandos Complejos-----------------

@bot.command(aliases=['8ball','8b'])
async def bolaocho(ctx,*,question):
	Respuestas=['No tengo idea.',
    			'Probablemente no.',
    			'No lo se.',
    			'Probable.',
        		'Claro que si, ¡Campeon!',
        		'Seguro que si.',
        		'Esta decidido que es asi.',
        		'Sin duda.',
        		'Si - Definitivamente.',
        		'Puedes estar seguro que si.',
        		'Como yo lo veo, si.',
        		'Muy Probable',
        		'Perspectiva Buena',
        		'¡Si!',
        		'¡No!',
        		'¡Los signos apuntan al si!',
        		'Pregunta muy confuza, reintenta de nuevo.',
        		'Mejor no te dire lo que yo se...',
        		'No puedo predecirlo Ahora :(.',
        		'Concentrate y preguntamelo de nuevo.',
        		"Mejor no esperes buenas vibras.",
        		'Mi respuesta es NO.',
        		'Mis fuentes dicen que no.',
        		'Tengo una perspectiva poco favorable.',
        		'Muy Dudoso']
	await ctx.send(f":8ball: Pregunta: {question}\n:8ball: Respuesta: {random.choice(Respuestas)}")

@bot.command(aliases=['joke'])
async def chiste(ctx):
	Respuestas=['¿Cual es el colmo de un calvo?... Tener ideas descabelladas',
    			'¿Cual es el colmo de un ciego?... Vivir en el Novenove',
    			'¿Tienen libros sobre el cansancio?.. Sí, pero ahora mismo no hay, ¡están todos agotados!',
    			'Nik me robo el chiste.',
    			'¿Qué le dice un pez a otro?... ¡Nada!',
        		'Paciente: Doctor, me duele aquí. \n Doctor: Pues póngase allí. \n Paciente: Doctor, me sigue doliendo. \n Doctor: Doliendo, deje de seguir al paciente.'
        		'Hijo: Papa, ¿soy adoptado? \n Padre: ¿Tú crees que te habríamos elegido a ti?'
        		'¿Cuál es el colmo de Batman? \n Que le Robin.'
        		'¿Qué pasa si un elefante se para sobre una pata? \n Que un pato se quedará viudo.'
        		'¿Cómo se escribe sintaxis? \n Con Uber.'
        		'¿Cómo se dice ‘espejo’ en chino? \n Aitoiyo.'
        		'¡Mamá, mamá, he sacado un 10! \n ¡Ah, sí! ¿En qué asignatura?\n En varias. Un 3 en Matemáticas, un 2 en Lengua, un 3 en Inglés y un 2 en Historia.',
        		'¿Cuál es el colmo de un ladrón? \n Llamarse Esteban Dido.',
        		'¿Cuál es el colmo de un tuerto? \n Llamarse Casimiro.',
        		'La maestra pregunta en clase: \n Laurita, ¿qué planeta va después de Marte? \n Miércoles.',
        		'¿Por qué las focas miran siempre hacia arriba? \n ¡Porque ahí están los focos!',
        		'El profesor le dice al estudiante después de haberle corregido la tarea: Tu trabajo me ha conmovido. \n El estudiante, sorprendido, le pregunta: ¿Y eso por qué profesor? \n El profesor con cara de burla le dice: Porque me dio mucha pena.',
        		'¿Qué le dice un techo a otro? \n Techo de menos.',
        		'Abuelo, ¿por qué estás delante del ordenador con los ojos cerrados? \n Es que Windows me ha dicho que cierre las pestañas.',
        		'¿Qué hace un perro con un taladro? \n Taladrando.',
        		'¿Qué le dice una gallina deprimida a otra gallina deprimida? \n Necesitamos apoyo.',
        		'Mamá, en el cole me llaman despistado. \n Niño, que esta no es tu casa.',
        		'Papá, papá, ¿puedo ir al cine? \n Sí, Jaimito, pero no entres.',
        		'En clase le preguntan a Jaimito: ¡A ver, Jaimito, ¿de qué signo es tu madre? \n Pues debe de ser de exclamación porque se pasa todo el día gritándome.',
        		'no se me ocurrio que añadir aqui xdddxdxxdx, ayuda estoy cansado',]
	await ctx.send(random.choice(Respuestas))

#---------Aviso del Estado del Bot------------

@bot.event
async def on_ready():
	print("Funcionando :3")

#----------Codigo Principal-------------------

bot.run('AGREGA AQUI EL CODIGO DEL BOT PARA CORRERLOS')