
from models.article import Article
from models.utilisateur import Utilisateur
from services.recommandeur import RecommandeurIA
from services.chatbot import ChatbotIA

if __name__ == "__main__":
    print("=== Système e-commerce IA ===\n")

    user = Utilisateur(1, "Justin", "justin@example.com", "motdepasse123")
    user.preferences = {"categories": ["Sport", "Tech"]}

    article1 = Article(1, "Chaussure Sport", 49.99, "42", "chaussure.jpg", "Sport")
    article2 = Article(2, "Casque Audio", 89.99, "N/A", "casque.jpg", "Tech")

    commande = user.passer_commande([article1, article2])
    print(" Commande effectuée :\n")
    print(commande.afficher_commande())

    print("\n Historique de commandes :")
    for historique in user.consulter_historique():
        print(historique)

    ia = RecommandeurIA(modeleIA="FakeMLModel")
    suggestions = ia.generer_suggestions(user)
    print("\n Suggestions IA :")
    for article in suggestions:
        print(article.afficher_details())

    bot = ChatbotIA()
    print("\n Chatbot :")
    question = "livraison"
    print(f"Q: {question}")
    print("A:", bot.repondre(question))
