# Atmos Sweep: Generates a 10-point baseline from 1km to 10km
sweep:
	@echo "📡 Starting Sovereign Altitude Sweep..."
	@for alt in 1000 2000 3000 4000 5000 6000 7000 8000 9000 10000; do \
		PYTHONPATH=src python -m atmos.main -a $$alt -j; \
	done
	@echo "✅ Sweep Complete. Running Health Check..."
	@./health.sh


