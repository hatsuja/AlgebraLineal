-- === MOTOR DE GENERACIÓN MATEMÁTICA EXACTA ===
local TAMANIO_BLOQUE = 4
local ultimaPosicionZ = 0	 -- El primer bloque iniciará en Z = 0
local contadorBloques = 1 -- Iniciamos a contar desde el bloque 1

-- Función para crear bloques basados en la Matriz de Estados
local function crearBloque(zCoord)
	local bloque = Instance.new("Part")
	bloque.Size = Vector3.new(TAMANIO_BLOQUE, 1, TAMANIO_BLOQUE)
	-- Se coloca exactamente en X=0, Y=0, y Z basada en la multiplicación escalar
	bloque.Position = Vector3.new(0, 0, zCoord) 
	bloque.Anchored = true
	bloque.Parent = game.Workspace

	-- LÓGICA MATEMÁTICA: Patrón cíclico (Azul, Azul, Rojo...)
	-- Si el número de bloque dividido para 3 tiene residuo 0 (es decir, es múltiplo de 3)
	if contadorBloques % 3 == 0 then
		-- ESTADO 2: Trampa (Rojo)
		bloque.BrickColor = BrickColor.new("Bright red")
		bloque.Material = Enum.Material.Neon
		bloque.Name = "Trampa"

		-- Evento letal
		bloque.Touched:Connect(function(objetoTocado)
			local personaje = objetoTocado.Parent
			local humano = personaje:FindFirstChildOfClass("Humanoid")
			if humano then
				humano.Health = 0 -- Muere instantáneamente
			end
		end)
	else
		-- ESTADO 1: Camino (Azul)
		bloque.BrickColor = BrickColor.new("Bright blue")
		bloque.Material = Enum.Material.Neon
		bloque.Name = "Camino"
	end

	-- Aumentamos el contador para la siguiente iteración
	contadorBloques = contadorBloques + 1
end

-- 1. Generamos los primeros 20 bloques iniciales con la nueva regla
for i = 1, 20 do
	crearBloque(ultimaPosicionZ)
	ultimaPosicionZ = ultimaPosicionZ + TAMANIO_BLOQUE
end

-- 2. Bucle principal que detecta el movimiento del jugador
task.spawn(function()
	while true do
		task.wait(0.1)

		-- Busca tu personaje específico o cualquier modelo de jugador
		local personaje = game.Workspace:FindFirstChild("lexjuan") or game.Workspace:FindFirstChildOfClass("Model")
		if personaje and personaje:FindFirstChild("HumanoidRootPart") then
			local root = personaje.HumanoidRootPart

			-- Sensor de proximidad: si te acercas al final del camino, genera otro bloque
			if root.Position.Z > (ultimaPosicionZ - 30) then
				crearBloque(ultimaPosicionZ)
				ultimaPosicionZ = ultimaPosicionZ + TAMANIO_BLOQUE
			end
		end
	end
end)
