db.auth('admin', 'password123')

db = db.getSiblingDB('celestial_wordforge')

db.createUser({
    user: 'admin',
    pwd: 'password123',
    roles: [
        {
            role: 'readWrite',
            db: 'celestial_wordforge'
        }
    ]
})

// Create users collection
db.createCollection('users')

// Create unique index on email field
db.users.createIndex({ "email": 1 }, { unique: true })
